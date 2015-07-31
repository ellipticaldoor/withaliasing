from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from blog import views, views_panel


urlpatterns = patterns(
	'',

	# panel views
	url(r'^add_entry/$', login_required(views_panel.AddEntryView.as_view()), name='add_entry'),
	url(r'^all_entries/$', login_required(views_panel.AllEntriesView.as_view()), name='all_entries'),
	url(r'^(?P<category>[-\w]+)/(?P<slug>.*)/edit$', views_panel.UpdateEntryView.as_view(), name='edit_entry'),

	# url views
	url(r'^$', views.BlogView.as_view(), name='blog'),
	url(r'^games/$', views.GamesView.as_view(), name='games'),
	url(r'^howtos/$', views.HowtosView.as_view(), name='howtos'),
	url(r'^(?P<category>[-\w]+)/$', views.CategoryView.as_view(), name='category'),
	url(r'^(?P<category>[-\w]+)/(?P<slug>.*)/$', views.EntryView.as_view(), name='entry'),
)
