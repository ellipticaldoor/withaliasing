from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = patterns('',)


if settings.DEBUG:
	import debug_toolbar
	from django.conf.urls.static import static

	urlpatterns += patterns('',
		url(r'^debug/', include(debug_toolbar.urls)),
	) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += patterns(
	'',
	url(r'^admin/', include(admin.site.urls)),

	url(r'^', include('blog.urls')),
)
