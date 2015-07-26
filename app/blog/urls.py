from django.conf.urls import patterns, url

from blog import views


urlpatterns = patterns(
	'',
	url(r'^$', views.BlogView.as_view(), name='blog'),
)
