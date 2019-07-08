from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    titulo1 = "Titulo"
    titulo2 = "Titulo"
    texto2 = "Mais uma página"
    texto1 = "Parte de uma página"

    return render_template("teste.html", titulo1=titulo1)

@app.route("/novo")
def nova_pag():
    lista = ["um", "dois", "tres", "quatro"]
 
    return render_template("nova_pag.html", titulo1=titulo1, titulo2=titulo2,
                                            texto1=texto1, texto2=texto2, 
                                            lista=lista) 


@app.route("/lista")
def pagina_1():
    lista_dir = os.listdir("static/files/")
    return render_template("lista.html", lista_dir=lista_dir)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234)
