from db.run_sql import run_sql

from models.film import Film

def save(film):
    sql = "INSERT INTO films(title, director_id, distributor_id, stock_quantity, buying_price, selling_price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [film.title, film.director.id, film.distributor.id, film.stock_quantity, film.buying_price, film.selling_price]
    results = run_sql(sql, values)
    film.id = results[0]['id']
    return film
