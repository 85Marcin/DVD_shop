from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.director import Director
from models.distributor import Distributor
from models.film import Film

import repositories.film_repository as film_repository
import repositories.distributor_repository as distributor_repository
import repositories.director_repository as director_repository


films_blueprint = Blueprint("films", __name__)


@films_blueprint.route("/films")
def films():
    films = film_repository.select_all()
    return render_template("stock/index.html", films = films)

@films_blueprint.route("/film")
def new():
    directors = director_repository.select_all()
    distributors = distributor_repository.select_all()
    return render_template("film/new.html", directors=directors, distributors=distributors)

@films_blueprint.route("/film", methods=['POST'])
def add_item():
    title = request.form['title']
    director_id = request.form['director']
    distributor_id = request.form['distributor']
    quantity = request.form ['quantity']
    buying_price = request.form ['buying_price']
    selling_price = request.form ['selling_price']
    director = director_repository.select(director_id)
    distributor = distributor_repository.select(distributor_id)
  
    

    film = Film(title, director, distributor, quantity, buying_price, selling_price)
    film_repository.save(film)
    return redirect("/films")

@films_blueprint.route("/films/<id>/delete", methods=['POST'])
def delete(id):
    film_repository.delete(id)
    return redirect('/films')

@films_blueprint.route("/films/<id>/edit")
def edit(id):
    film = film_repository.select(id)
    director = film.director
    distributor = film.distributor
    return render_template("/film/edit.html", film=film, director=director, distributor=distributor)

@films_blueprint.route("/films/<id>/edit", methods=['POST'])
def update_film(id):
    film = film_repository.select(id)
    film.title = request.form['title']
    film.stock_quantity = request.form ['quantity']
    film.buying_price = request.form ['buying_price']
    film.selling_price = request.form ['selling_price']

    film_repository.update(film)

    return redirect("/films")









