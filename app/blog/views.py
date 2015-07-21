from django.views.generic import TemplateView


class FrontView(TemplateView):
	template_name = 'blog/front.html'
