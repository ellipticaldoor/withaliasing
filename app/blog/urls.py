from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from blog import views


urlpatterns = patterns(
	'',
	url(r'^$', views.BlogView.as_view(), name='blog'),

	url(r'^games/$', views.GamesView.as_view(), name='games'),
	url(r'^(?P<category>[-\w]+)/$', views.CategoryView.as_view(), name='category'),
	url(r'^(?P<category>[-\w]+)/(?P<slug>.*)/$', views.EntryView.as_view(), name='entry'),
)
