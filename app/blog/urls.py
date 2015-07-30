from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from blog import views, views_panel


urlpatterns = patterns(
	'',

	# panel views
	url(r'^new_entry/$', login_required(views_panel.NewEntryView.as_view()), name='new_entry'),

	# url views
	url(r'^$', views.BlogView.as_view(), name='blog'),
	url(r'^games/$', views.GamesView.as_view(), name='games'),
	url(r'^howtos/$', views.HowtosView.as_view(), name='howtos'),
	url(r'^(?P<category>[-\w]+)/$', views.CategoryView.as_view(), name='category'),
	url(r'^(?P<category>[-\w]+)/(?P<slug>.*)/$', views.EntryView.as_view(), name='entry'),
)
