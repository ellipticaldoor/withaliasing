from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from blog import views


urlpatterns = patterns(
	'',
	url(r'^$', views.BlogView.as_view(), name='blog'),

	url(r'^(?P<entry_type>[-\w]+)/(?P<slug>.*)/$', views.EntryView.as_view(), name='entry'),
)
