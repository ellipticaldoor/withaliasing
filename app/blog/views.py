from django.views.generic import DetailView, ListView

from blog.models import Entry


class BlogView(ListView):
	template_name = 'blog/entry_list.html'
	queryset = Entry.objects.published()
	paginate_by = 5


class EntryView(DetailView):
	template_name = 'blog/entry.html'

	def get_queryset(self):
		return Entry.objects.by_entry(self.kwargs['entry_type'], self.kwargs['slug'])
