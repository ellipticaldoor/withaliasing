from django.conf.urls import patterns, url

from blog import views


urlpatterns = patterns(
	'',
	url(r'^$', views.FrontView.as_view(), name='front', kwargs={'tab':'top'}),
)
