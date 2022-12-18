from flask import Flask, render_template

from controllers.controller import films_blueprint

app = Flask(__name__)



app.register_blueprint(films_blueprint)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)