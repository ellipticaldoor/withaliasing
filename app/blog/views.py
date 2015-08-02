from django.views.generic import DetailView, ListView
from django.http import Http404

from blog.models import Category, Entry


class CategoryView(ListView):
	template_name = 'blog/entry_list.html'
	paginate_by = 3

	def get(self, request, *args, **kwargs):
		if request.is_ajax():
			self.template_name = 'blog/ajax/entry_list.html'

		return super(CategoryView, self).get(request, *args, **kwargs)

	def get_queryset(self):
		if self.kwargs['current'] == 'blog':
			entries = Entry.objects.published()
		else:
			category = self.kwargs['category']
			entries = Entry.objects.by_category(category)

			if not entries:
				try:
					Category.objects.get(slug=category)
				except:
					raise Http404

		return entries

	def get_context_data(self, **kwargs):
		context = super(CategoryView, self).get_context_data(**kwargs)

		if self.kwargs['current'] == 'blog':
			context['list_url'] = '/'
		else:
			category_list = self.kwargs['category']
			context['category_list'] = category_list
			context['list_url'] = '/%s/' % category_list

		context['categories'] = Category.objects.all()

		return context


class GamesView(ListView):
	template_name = 'blog/category/games.html'
	queryset = Entry.objects.by_category('games')


class HowtosView(ListView):
	template_name = 'blog/category/howtos.html'
	queryset = Entry.objects.by_category('howtos')


class EntryView(DetailView):
	template_name = 'blog/entry.html'

	def get_queryset(self):
		return Entry.objects.by_entry(self.kwargs['category'], self.kwargs['slug'])
