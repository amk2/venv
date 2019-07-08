"""
requests and upload

"""

from flask import Flask, request
from ex03_pizzaria import pizzaria

app = Flask(__name__)


"""
Exemplo de chamada POST
curl http://127.0.0.1:5000/trata -d "num1=1&num2=2"

url_for('static', filename='style.css')

"""

template1 = open("pizza1.html").read()
template2 = open("pizza2.html").read()


@app.route("/")
def index():
    titulo= "Curso Python - Pizzaria"
    return template1.format(titulo=titulo)


@app.route("/pizza2", methods =["GET"])
def trata():
    titulo= "Curso Python - Pizzaria"
    pizza_escolhida = request.args["pizza"]
    ingredientes = []
    if "queijo" in request.args:
        ingredientes.append("queijo")
    if "cebola" in request.args:
        ingredientes.append("cebola")
    if "ovo" in request.args:
        ingredientes.append("ovo")
    if "pimentao" in request.args:
        ingredientes.append("pimentao")
    massa = request.args["massa"]
    borda = request.args["borda"]
    nome = request.args["nome"]
    tel = request.args["tel"]
    total = pizzaria(pizza_escolhida, ingredientes, massa=massa, borda=borda)
    ingredientes_str = (",").join(ingredientes)
    return template2.format(titulo=titulo, pizza_escolhida=pizza_escolhida, borda=borda, massa=massa, total=total,ingredientes_str=ingredientes_str, nome=nome, tel=tel)

if __name__ == "__main__":
    app.run()
