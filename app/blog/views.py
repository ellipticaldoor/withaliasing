from django.views.generic import DetailView, ListView

from blog.models import Entry


class BlogView(ListView):
	template_name = 'blog/entry_list.html'
	queryset = Entry.objects.published()
	paginate_by = 5


class GamesView(ListView):
	template_name = 'blog/category/games.html'
	queryset = Entry.objects.by_category('games')


class HowtosView(ListView):
	template_name = 'blog/category/howtos.html'
	queryset = Entry.objects.by_category('howtos')


class CategoryView(ListView):
	template_name = 'blog/entry_list.html'
	paginate_by = 5

	def get_queryset(self):
		return Entry.objects.by_category(self.kwargs['category'])


class EntryView(DetailView):
	template_name = 'blog/entry.html'

	def get_queryset(self):
		return Entry.objects.by_entry(self.kwargs['category'], self.kwargs['slug'])
