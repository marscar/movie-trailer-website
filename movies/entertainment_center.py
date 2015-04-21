import fresh_tomatoes
import	media

star_wars = media.Movie("Star Wars VII",
	"The dark side is awakening",
	('http://i.kinja-img.com/gawker-media/image/upload/s--2lEyekmH--/c_fit,'
		'fl_progressive,q_80,w_636/19fk32sw3nt1wjpg.jpg'),
	"https://www.youtube.com/watch?v=OMOVFvcNfvE")


avatar = media.Movie("Avatar",
	"A marine in an alien planet",
	"http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")


jupiter = media.Movie("Jupiter Ascending",
	('Jupiter Jones was born under a night sky, with signs predicting she was'
		' destined for great things.'),
	("http://cdn.screenrant.com/wp-content/uploads/Jupiter-Ascending-Channing-"
		"Tatum-poster.jpg"),
	"https://www.youtube.com/watch?v=ZoCyL_Pqzu8")


Harley_and_Marlboro = media.Movie("Harley Davidson and Marlboro man",
	('Biker Harley Davidson and his surly cowboy buddy,'
		' Marlboro decide robbing a bank.'),
	('http://upload.wikimedia.org/wikipedia/en/0/04/Harley_davidson_and'
		'_the_marlboro_man_movie_poster.jpg'),
	"https://www.youtube.com/watch?v=g8K34N604Iw")


hobbit = media.Movie("The Hobbit",
	"An epic adventurous journey in search of a magic ring.",
	'http://i.huffpost.com/gen/784488/thumbs/o-THE-HOBBIT-POSTER-570.jpg?7',
	"https://www.youtube.com/watch?v=G0k3kHtyoqc")


gladiator = media.Movie("The Gladiator",
	"A Roman Imperial Army general turns into a gladiator.",
	"http://movieartarena.com/images/10005231.1.jpg",
	"https://www.youtube.com/watch?v=icWR_kCmfUU")


movies = [star_wars, avatar, jupiter, Harley_and_Marlboro, hobbit, gladiator]

fresh_tomatoes.open_movies_page(movies)