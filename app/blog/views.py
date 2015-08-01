from django.views.generic import DetailView, ListView

from blog.models import Entry


class CategoryView(ListView):
	template_name = 'blog/entry_list.html'
	paginate_by = 2

	def get(self, request, *args, **kwargs):
		if request.is_ajax():
			self.template_name = 'blog/ajax/entry_list.html'

		return super(CategoryView, self).get(request, *args, **kwargs)

	def get_queryset(self):
		if self.kwargs['current'] == 'blog':
			return Entry.objects.published()
		else:
			return Entry.objects.by_category(self.kwargs['category'])

	def get_context_data(self, **kwargs):
		context = super(CategoryView, self).get_context_data(**kwargs)

		if self.kwargs['current'] == 'blog':
			context['list_url'] = '/'
		else:
			list_category = self.kwargs['category']
			context['category'] = list_category
			context['list_url'] = '/%s/' % list_category

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
