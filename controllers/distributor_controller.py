from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.distributor import Distributor

import repositories.distributor_repository as distributor_repository


distributors_blueprint = Blueprint("distributors", __name__)

@distributors_blueprint.route("/distributors")
def distributors():
    distributors = distributor_repository.select_all()
    return render_template("distributor/new.html", distributors=distributors)

@distributors_blueprint.route("/distributors", methods=['POST'])
def add_distributor():
    distributor_name = request.form['distributor']
    distributor = Distributor(distributor_name)
    distributor_repository.save(distributor)
    return redirect("/distributors")

@distributors_blueprint.route("/distributors/<id>/delete", methods=['POST'])
def delete(id):
    distributor_repository.delete(id)
    return redirect("/distributors")








