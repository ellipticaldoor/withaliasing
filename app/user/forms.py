from django import forms
from django.contrib.auth.forms import AuthenticationForm


def set_user_form_attrs(self):
		self.fields['username'].widget.attrs.update({
				'autofocus': 'autofocus',
				'required': 'required',
				'placeholder': 'user',
				'autocapitalize': "off",
				'spellcheck': "off"
			})
		self.fields['password'].widget.attrs.update({
				'required': 'required',
				'placeholder': 'password'
			})
		return self


class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		set_user_form_attrs(self)

	username = forms.CharField(label='', max_length=16, )
	password = forms.CharField(label='', widget=forms.PasswordInput)
