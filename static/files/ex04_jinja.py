from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


@app.route("/lista")
def pagina_1():
    lista_dir = os.listdir("static/files/")
    return render_template("lista.html", lista_dir=lista_dir)


if __name__ == "__main__":
    app.run()
