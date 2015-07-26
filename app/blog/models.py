from django.db import models
from django.utils.text import slugify

from user.models import User
from core.core import _createId
from core.video_embed import CustomVideoExtension

from markdown import markdown


class Category(models.Model):
	slug = models.SlugField(primary_key=True, max_length=40)

	class Meta:
		verbose_name_plural = 'Categories'
		ordering = ['slug']

	def __str__(self): return self.slug


class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(status='published')

	def by_category(self, category):
		return self.filter(category=category, status='published')

	def by_type(self, entry_type):
		return self.filter(slug=slug, status='published')

	def by_entry(self, entry_type, slug):
		return self.filter(entry_type=entry_type, slug=slug, status='published')


class Entry(models.Model):
	STATUS_CHOICES = (
		('draft', 'draft'),
		('published', 'published'),
	)

	ENTRY_TYPE_CHOICES = (
		('post', 'post'),
		('howto', 'howto'),
		('game', 'game'),
	)

	def get_image(instance, filename):
		if not hasattr(instance.entryid, 'decode'): entryid = instance.entryid
		else: entryid = instance.entryid.decode('utf-8')
		return 'entry/%s.png' % (entryid)

	entryid = models.CharField(primary_key=True, max_length=16, default=_createId)
	user = models.ForeignKey(User, related_name='entries')
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	body_html = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to=get_image, blank=True, null=True)
	entry_type = models.CharField(db_index=True, max_length=10, choices=ENTRY_TYPE_CHOICES, default='post')
	status = models.CharField(db_index=True, max_length=10, choices=STATUS_CHOICES, default='draft')
	category = models.ForeignKey(Category, related_name='categories')
	created = models.DateTimeField(auto_now_add=True)

	objects = EntryQuerySet.as_manager()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title.replace(' ', '_'))
		self.body_html = markdown(self.body, safe_mode=True, extensions=[CustomVideoExtension()])
		super(Entry, self).save(*args, **kwargs)

	@models.permalink
	def get_absolute_url(self):
		return ('entry', [self.entry_type, self.slug,])

	def __str__(self): return self.title

	class Meta:
		verbose_name_plural = 'Entries'
		ordering = ['-created']
