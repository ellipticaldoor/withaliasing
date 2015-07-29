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

	@models.permalink
	def get_absolute_url(self):
		return ('category', [self.pk,])

	def __str__(self):
		return self.slug


class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(status='published')

	def by_category(self, category):
		return self.filter(category=category, status='published')

	def by_entry(self, category, slug):
		return self.filter(category=category, slug=slug, status='published')


class Entry(models.Model):
	STATUS_CHOICES = (
		('draft', 'draft'),
		('published', 'published'),
	)

	def get_image(instance, filename):
		if not hasattr(instance.entryid, 'decode'): entryid = instance.entryid
		else: entryid = instance.entryid.decode('utf-8')
		return 'entry/%s.jpg' % (entryid)

	entryid = models.CharField(primary_key=True, max_length=16, default=_createId)
	user = models.ForeignKey(User, related_name='entries')
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	body_html = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to=get_image, blank=True, null=True)
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
		return ('entry', [self.category.pk, self.slug,])

	@models.permalink
	def get_category_url(self):
		return ('category', [self.category.pk,])

	def get_image_url(self):
		return '/m/%s' % (self.image)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Entries'
		ordering = ['-created']
