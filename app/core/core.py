from binascii import hexlify
from os import urandom
from PIL import Image

from django.forms import ClearableFileInput


class ImageInput(ClearableFileInput):
	template_with_initial = (
		'<div id="image_entry_edit">'
			'<img src="%(initial_url)s">'
			'<label for="image-clear_id">delete</label>'
			'<input id="image-clear_id" name="image-clear" type="checkbox"><br>'
			'%(input)s'
		'</div>'
	)

def _createId():
	return hexlify(urandom(3))
