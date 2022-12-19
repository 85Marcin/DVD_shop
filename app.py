from flask import Flask, render_template

from controllers.film_controller import films_blueprint
from controllers.distributor_controller import distributors_blueprint
from controllers.director_controller import directors_blueprint

app = Flask(__name__)



app.register_blueprint(films_blueprint)
app.register_blueprint(distributors_blueprint)
app.register_blueprint(directors_blueprint)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)