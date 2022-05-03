import requests
import random

def header():
    API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwOWMyYzY5NzU3MmQyOThkMzFmYTQ5NzRmY2JkODNiNiIsInN1YiI6IjYyNWZiOTJhYTUwNDZlMTFlMjBkZmVhZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.r4UM54RFGq7NxDt7SXuO_oVtgwVrCsvH0POBgVryJto"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    return headers

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    response = requests.get(endpoint, headers=header())
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    random.shuffle(data["results"])
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(endpoint, headers=header())
    return response.json()

def get_single_movie_cast(movie_id, how_many):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    response = requests.get(endpoint, headers=header())
    return response.json()["cast"][:how_many]

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    response = requests.get(endpoint, headers=header())
    response.raise_for_status()
    return response.json()

