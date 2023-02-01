from faker import Faker
import random

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.play_count = 0
    
    def __str__(self):
        return f'{self.title} ({self.year})'
    
    def play(self):
        self.play_count = self.play_count + 1

class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode
    
    def __str__(self):
        return "%s S%02dE%02d" % (self.title, self.season, self.episode)

def generate_series_and_moveies(how_many):
    faker = Faker()
    
    genres = ['Comedy', 'Horror', 'Drama', 'Thriller', 'Criminal', 'Fantasy', 'Sci-Fi']
    
    movie_list = []
    
    for _ in range(how_many):
        series = random.randint(0, 1)
        title = faker.word()
        year = faker.year()
        genre_index = random.randint(0, len(genres) - 1)
        genre = genres[genre_index]
        if series == 0:
            movie = Movie(title, year, genre)
            movie_list.append(movie)
        else:
            season = random.randint(1, 8)
            episode = random.randint(1, 99)
            series = Series(season, episode, title, year, genre)
            movie_list.append(series)
    
    return movie_list

movie_list = generate_series_and_moveies(20)

def get_movies():
    movies = []
    for movie in movie_list:
        if type(movie) is Movie:
            movies.append(movie)
    movies.sort(key = lambda movie : movie.title)
    return movies

def get_series():
    movies = []
    for movie in movie_list:
        if type(movie) is Series:
            movies.append(movie)
    movies.sort(key = lambda movie : movie.title)
    return movies

def search(title):
    for movie in movie_list:
        if movie.title == title:
            return movie
    return None

def generate_views():
    movie = random.choice(movie_list)
    random_play_count = random.randint(1,100)
    movie.play_count = movie.play_count + random_play_count

def ten_generate_views():
    for _ in range(10):
        generate_views()

def top_titles(count, content_type):
    movies = []
    if content_type == 'movie':
        movies = get_movies()
    elif content_type == 'series':
        movies = get_series()
    
    if len(movies) == 0:
        return []

    movies.sort(key = lambda movie : movie.play_count)
    return movies[:count]

print ("TEST PLAY MOVIES")
for movie in get_movies():
    movie.play()

print ("TEST PLAY SERIES")
for movie in get_series():
    movie.play()

print ("TEST SEARCH")
found_movie = search(movie_list[5].title)
if found_movie:
    print (f"Found a movie {found_movie.title}")

generate_views()
ten_generate_views()

top_movies = top_titles(2, 'movie')
top_movies = top_titles(2, 'series')
