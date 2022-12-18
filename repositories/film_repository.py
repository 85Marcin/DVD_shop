from db.run_sql import run_sql

from models.film import Film

import repositories.director_repository as director_repository
import repositories.distributor_repository as distributor_repository

def save(film):
    sql = "INSERT INTO films(title, director_id, distributor_id, stock_quantity, buying_price, selling_price, profit) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [film.title, film.director.id, film.distributor.id, film.stock_quantity, film.buying_price, film.selling_price, film.profit]
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
        film = Film(row['title'], director, distributor,row['stock_quantity'], row['buying_price'], row['selling_price'], row['id'])
        films.append(film)
    return films
