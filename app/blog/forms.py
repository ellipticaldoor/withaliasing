from django import forms

from blog.models import Entry, Category
from core.core import ImageInput


class EntryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(EntryForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({
				'required': 'required',
				'placeholder': 'título',
				'autocomplete': 'off',
			})
		self.fields['body'].widget.attrs.update({
				'required': 'required',
				'autofocus': 'autofocus',
				'placeholder': 'post',
				'autocomplete': 'off',
			})
		self.fields['image'].widget.attrs.update({'accept': 'image/*'})
		self.fields['category'].widget.attrs.update({'required': 'required'})

	title = forms.CharField(label='', max_length=100)
	body = forms.CharField(label='', widget=forms.Textarea)
	image = forms.ImageField(label='', widget=ImageInput, required=False)
	category = forms.ModelChoiceField(label='', queryset=Category.objects.all())
	status = forms.ChoiceField(label='', choices=(('draft', 'draft'),('published', 'published'),))

	class Meta:
		model = Entry
		fields = ('title', 'body', 'image', 'status', 'category',)


class CategoryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CategoryForm, self).__init__(*args, **kwargs)
		self.fields['slug'].widget.attrs.update({
				'autofocus': 'autofocus',
				'required': 'required',
				'placeholder': 'category name',
				'autocomplete': 'off',
			})

	slug = forms.CharField(label='', max_length=40)

	class Meta:
		model = Category
		fields = ('slug',)
