from django.views.generic.edit import CreateView, UpdateView

from blog.forms import EntryForm


class NewEntryView(CreateView):
	template_name = 'blog/panel/new_entry.html'
	form_class = EntryForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()

		if obj.draft:
			return HttpResponseRedirect('/created')
		else:
			return HttpResponseRedirect(obj.get_absolute_url())
