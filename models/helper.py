import repositories.film_repository as film_repository
import repositories.distributor_repository as distributor_repository
import repositories.director_repository as director_repository

def get_lists():
    directors = director_repository.select_all()
    distributors = distributor_repository.select_all()
    films = film_repository.select_all()
    genres = []
    for film in films:
        if film.genre not in genres:
            genres.append(film.genre)
    return directors, distributors, genres
