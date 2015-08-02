from django.conf.urls import patterns, url

from user.forms import LoginForm


urlpatterns = patterns(
	'',
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html', 'authentication_form': LoginForm}, name="login"),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name="logout"),
)
