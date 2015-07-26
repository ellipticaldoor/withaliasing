from django.db import models
from django.utils.text import slugify

from user.models import User
from core.core import _createId
from core.video_embed import CustomVideoExtension

from django_resized import ResizedImageField
from markdown import markdown


class Post(models.Model):
	def get_image(instance, filename):
		if not hasattr(instance.postid, 'decode'): postid = instance.postid
		else: postid = instance.postid.decode('utf-8')
		return 'post/%s.png' % (postid)

	postid = models.CharField(primary_key=True, max_length=16, default=_createId)
	user = models.ForeignKey(User, related_name='posts')
	sub = models.ForeignKey(Sub, related_name='posts')
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	body = models.TextField(max_length=10000)
	body_html = models.TextField(blank=True, null=True)
	image = ResizedImageField(size=[950, 950], quality=90, upload_to=get_image, blank=True, null=True)
	draft = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	objects = PostQuerySet.as_manager()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title.replace(' ', '_'))
		if not self.slug: self.slug = '_'
		self.body_html = markdown(self.body, safe_mode=True, extensions=[CustomVideoExtension())
		super(Post, self).save(*args, **kwargs)

	def get_absolute_url(self):
		if not hasattr(self.pk, 'decode'): postid = self.pk
		else: postid = self.pk.decode('utf-8')
		return '/post/%s/%s/' % (postid, self.slug)

	def get_edit_url(self): return '%sedit/' % (self.get_absolute_url())

	def __str__(self): return self.title
