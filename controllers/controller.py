from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.film_repository as film_repository


films_blueprint = Blueprint("films", __name__)

@films_blueprint.route("/films")
def films():
    films = film_repository.select_all()
    return render_template("stock/index.html", films = films)

@films_blueprint.route("/new")
def new():
    return render_template("new/new.html")
