import markdown, json
from urllib.request import urlopen
from markdown.util import etree


class CustomVideoExtension(markdown.Extension):
	def add_inline(self, md, name, klass, re):
		pattern = klass(re)
		pattern.md = md
		pattern.ext = self
		md.inlinePatterns.add(name, pattern, '<reference')

	def extendMarkdown(self, md, md_globals):
		self.add_inline(md, 'vimeo', Vimeo,
			r'([^(]|^)https?://(www.|)vimeo\.com/(?P<vimeoid>\d+)\S*')
		self.add_inline(md, 'youtube', Youtube,
			r'([^(]|^)https?://www\.youtube\.com/watch\?\S*v=(?P<youtubeid>\S[^&/]+)')
		self.add_inline(md, 'youtube_short', Youtube,
			r'([^(]|^)https?://youtu\.be/(?P<youtubeid>\S[^?&/]+)?')


class Vimeo(markdown.inlinepatterns.Pattern):
	def handleMatch(self, m):
		return render_iframe(m.group('vimeoid'), 'vimeo')


class Youtube(markdown.inlinepatterns.Pattern):
	def handleMatch(self, m):
		return render_iframe(m.group('youtubeid'), 'youtube')


def render_iframe(data_id, player):
	a_container = etree.Element('a')

	if player == 'youtube':
		a_container.set('href', 'https://www.youtube.com/watch?v=%s' % data_id.replace(' ', ''))

		try:
			thumb_img_src = 'http://i.ytimg.com/vi/%s/maxresdefault.jpg' % data_id.replace(' ', '')
			urlopen(thumb_img_src)
		except:
			thumb_img_src = 'http://i.ytimg.com/vi/%s/hqdefault.jpg' % data_id.replace(' ', '')

	elif player == 'vimeo':
		a_container.set('href', 'https://vimeo.com/%s' % data_id.replace(' ', ''))

		video_json_info = urlopen('http://vimeo.com/api/v2/video/%s.json' % data_id.replace(' ', '')).read()
		thumb_img_src = json.loads(video_json_info.decode())[0]['thumbnail_large']


	a_container.set('target', '_blank')
	a_container.set('class', 'video_container')
	img = etree.SubElement(a_container, 'img')
	img.set('src', thumb_img_src )

	return a_container


def makeExtension(**kwargs):
	return VideoExtension(**kwargs)
