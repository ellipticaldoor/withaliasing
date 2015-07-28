from django.views.generic import DetailView, ListView

from blog.models import Entry


class BlogView(ListView):
	template_name = 'blog/entry_list.html'
	queryset = Entry.objects.published()
	paginate_by = 5

	def get_context_data(self, **kwargs):
		context = super(BlogView, self).get_context_data(**kwargs)
		context['nav_selected'] = 'blog'
		return context


class GamesView(ListView):
	template_name = 'blog/category/games.html'
	queryset = Entry.objects.by_category('games')

	def get_context_data(self, **kwargs):
		context = super(GamesView, self).get_context_data(**kwargs)
		context['nav_selected'] = 'games'
		return context


class HowtosView(ListView):
	template_name = 'blog/category/howtos.html'
	queryset = Entry.objects.by_category('howtos')

	def get_context_data(self, **kwargs):
		context = super(HowtosView, self).get_context_data(**kwargs)
		context['nav_selected'] = 'howtos'
		return context


class CategoryView(ListView):
	template_name = 'blog/entry_list.html'
	paginate_by = 5

	def get_queryset(self):
		return Entry.objects.by_category(self.kwargs['category'])


class EntryView(DetailView):
	template_name = 'blog/entry.html'

	def get_queryset(self):
		return Entry.objects.by_entry(self.kwargs['category'], self.kwargs['slug'])
