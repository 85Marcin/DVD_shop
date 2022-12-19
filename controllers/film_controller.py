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

@films_blueprint.route("/new")
def new():
    return render_template("new/new.html")

@films_blueprint.route("/new", methods=['POST'])
def add_item():
    title = request.form['title']
    director_name = request.form['director']
    distributor_name = request.form['distributor']
    quantity = request.form ['quantity']
    buying_price = request.form ['buying_price']
    selling_price = request.form ['selling_price']
    director = Director(director_name)
    director_repository.save(director)
    distributor = Distributor(distributor_name)
    distributor_repository.save(distributor)
    film = Film(title, director, distributor, quantity, buying_price, selling_price)
    film_repository.save(film)
    return redirect("/films")




