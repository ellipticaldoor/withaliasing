from django import forms

from blog.models import Entry
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
