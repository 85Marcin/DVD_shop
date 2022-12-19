from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.director import Director

import repositories.director_repository as director_repository

directors_blueprint = Blueprint("directors", __name__)

@directors_blueprint.route("/directors")
def directors():
    return render_template("director/new.html")

@directors_blueprint.route("/directors", methods=['POST'])
def add_distributor():
    director_name = request.form['director']
    director = Director(director_name)
    director_repository.save(director)
    return redirect("/directors")








    