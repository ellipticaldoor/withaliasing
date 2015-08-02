from django import forms

from blog.models import Entry, Category
from core.core import ImageInput


class EntryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(EntryForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({
				'autofocus': 'autofocus',
				'required': 'required',
				'placeholder': 'título'
			})
		self.fields['body'].widget.attrs.update({
				'required': 'required',
				'placeholder': 'post'
			})
		self.fields['image'].widget.attrs.update({'accept': 'image/*'})
		self.fields['category'].widget.attrs.update({'required': 'required'})

	image = forms.ImageField(widget=ImageInput, required=False)

	class Meta:
		model = Entry
		fields = ('title', 'body', 'image', 'category', 'status')


class CategoryForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CategoryForm, self).__init__(*args, **kwargs)
		self.fields['slug'].widget.attrs.update({
				'autofocus': 'autofocus',
				'required': 'required',
				'placeholder': 'category name'
			})

	slug = forms.CharField(label='', max_length=40)

	class Meta:
		model = Category
		fields = ('slug',)
