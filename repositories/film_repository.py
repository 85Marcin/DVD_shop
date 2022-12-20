from db.run_sql import run_sql

from models.film import Film

import repositories.director_repository as director_repository
import repositories.distributor_repository as distributor_repository

def save(film):
    sql = "INSERT INTO films(title, genre, director_id, distributor_id, stock_quantity, buying_price, selling_price, profit) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [film.title, film.genre ,film.director.id, film.distributor.id, film.stock_quantity, film.buying_price, film.selling_price, film.profit]
    results = run_sql(sql, values)
    film.id = results[0]['id']
    return film

def delete_all():
    sql = "DELETE FROM films"
    run_sql(sql)

def select_all():
    films =[]
    
    sql = "SELECT * FROM films"
    results = run_sql(sql)

    for row in results:
        director = director_repository.select(row['director_id'])
        distributor = distributor_repository.select(row['distributor_id'])
        film = Film(row['title'], row['genre'],director, distributor,row['stock_quantity'], row['buying_price'], row['selling_price'], row['id'])
        films.append(film)
    return films

def select(id):
    film = None
    sql = "SELECT * FROM films WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        director = director_repository.select(result['director_id'])
        distributor = distributor_repository.select(result['distributor_id'])
        film = Film(result['title'], result['genre'], director, distributor,result['stock_quantity'], result['buying_price'], result['selling_price'], result['id'] )
    return film

def delete(id):
    sql = "DELETE FROM films WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(film):
    sql = "UPDATE films SET (title, genre, director_id, distributor_id, stock_quantity, buying_price, selling_price) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"

    values = [film.title, film.genre, film.director.id, film.distributor.id, film.stock_quantity, film.buying_price, film.selling_price, film.id]
    run_sql(sql, values)

def filter_by_director(id):
    films_by_director = []
    sql = "SELECT * FROM films WHERE director_id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        for row in results:
            director = director_repository.select(row['director_id'])
            distributor = distributor_repository.select(row['distributor_id'])
            film = Film(row['title'], row['genre'],director, distributor,row['stock_quantity'], row['buying_price'], row['selling_price'], row['id'])
            films_by_director.append(film)
    return films_by_director

def filter_by_distributor(id):
    films_by_distributor = []
    sql = "SELECT * FROM films WHERE distributor_id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        for row in results:
            director = director_repository.select(row['director_id'])
            distributor = distributor_repository.select(row['distributor_id'])
            film = Film(row['title'], row['genre'], director, distributor,row['stock_quantity'], row['buying_price'], row['selling_price'], row['id'])
            films_by_distributor.append(film)
    return films_by_distributor


def filter_by_genre(genre):
    films_by_genre = []
    sql = "SELECT * FROM films WHERE genre = %s"
    values = [genre]
    results = run_sql(sql, values)

    if results:
        for row in results:
            director = director_repository.select(row['director_id'])
            distributor = distributor_repository.select(row['distributor_id'])
            film = Film(row['title'], row['genre'], director, distributor,row['stock_quantity'], row['buying_price'], row['selling_price'], row['id'])
            films_by_genre.append(film)
    return films_by_genre






