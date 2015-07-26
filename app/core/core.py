from binascii import hexlify
from os import urandom
from PIL import Image

from django.forms import ClearableFileInput


class ImageInput(ClearableFileInput):
	template_with_initial = (
		'<div id="image_post_edit"><div><img src="%(initial_url)s"></div>'
		'<input id="image-clear_id" name="image-clear" type="checkbox"> <label for="image-clear_id">borrar</label></div>'
		'%(input)s'
	)

def _createId():
	return hexlify(urandom(3))
