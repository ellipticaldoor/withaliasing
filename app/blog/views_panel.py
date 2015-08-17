from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from blog.models import Entry
from blog.forms import EntryForm, CategoryForm


class AddEntryView(CreateView):
	template_name = 'panel/entry_form.html'
	form_class = EntryForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()

		if obj.status == 'draft':
			return HttpResponseRedirect('/all_entries')
		else:
			return HttpResponseRedirect(obj.get_absolute_url())


class UpdateEntryView(UpdateView):
	template_name = 'panel/entry_form.html'
	form_class = EntryForm

	def get_queryset(self):
		return Entry.objects.by_user(self.request.user)

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.save()

		if obj.status == 'draft':
			return HttpResponseRedirect('/all_entries')
		else:
			return HttpResponseRedirect(obj.get_absolute_url())


class AllEntriesView(ListView):
	template_name = 'panel/all_entries.html'

	def get_queryset(self):
		return Entry.objects.by_user(self.request.user)


class AddCategoryView(CreateView):
	template_name = 'panel/category_form.html'
	form_class = CategoryForm
	success_url = '/all_entries'
