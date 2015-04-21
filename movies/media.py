import webbrowser

class Movie():
	""" This class provide a way to store movies and include a method 
	that show a trailer.

	Attributes:
		title: Movie title
		storyline: short description of the storyline
		poster_image_url: Link to the movie poster.
		trailer_youtube_url: link to the movie trailer.
	"""

	def __init__(self, movie_title, movie_storyline,
				 poster_image, trailer_youtube):
		"""Inits Movie with all reauired attributes"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		"""Open link to the trailer and executes the trailer"""
		webbrowser.open(self.trailer_youtube_url)