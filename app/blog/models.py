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

	def by_user(self, user):
		return self.filter(user=user)


class Entry(models.Model):
	STATUS_CHOICES = (
		('draft', 'draft'),
		('published', 'published'),
	)

	def get_image(instance, filename):
		if hasattr(instance.entryid, 'decode'):
			instance.entryid = instance.entryid.decode('utf-8')
		return 'entry/%s.jpg' % (instance.entryid)

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
		self.body_html = markdown(self.body, safe_mode=False, extensions=[CustomVideoExtension(), 'codehilite'], extension_configs={ 'codehilite': { 'linenums': 'False', 'css_class': 'highlight', }, })
		super(Entry, self).save(*args, **kwargs)

	@models.permalink
	def get_absolute_url(self):
		return ('entry', [self.category_id, self.slug,])

	@models.permalink
	def get_edit_url(self):
		return ('edit_entry', [self.category_id, self.slug,])

	@models.permalink
	def get_category_url(self):
		return ('category', [self.category_id,])

	def get_image_url(self):
		return '/m/%s' % (self.image)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Entries'
		ordering = ['-created']


class Image(models.Model):
	def get_image(instance, filename):
		if hasattr(instance.imageid, 'decode'):
			instance.imageid = instance.imageid.decode('utf-8')

		return 'image/%s.jpg' % (instance.imageid )

	imageid = models.CharField(primary_key=True, max_length=16, default=_createId)
	image = models.ImageField(upload_to=get_image, blank=True, null=True)
	title = models.CharField(max_length=100, unique=True)
	created = models.DateTimeField(auto_now_add=True)

	@models.permalink
	def get_absolute_url(self):
		# TODO: Finish to setup this url
		return '/photo.jpg'

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created']


class ImageEntryLink(models.Model):
	linkid = models.CharField(primary_key=True, max_length=33, blank=True)
	image = models.ForeignKey(Image, related_name='image_link')
	entry = models.ForeignKey(Entry, related_name='entry_link')
	created = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		self.linkid = '%s>%s' % (self.image_pk, self.entry_pk)
		super(ImageEntryLink, self).save(*args, **kwargs)

	def __str__(self):
		return self.linkid

	class Meta:
		ordering = ['-created']
