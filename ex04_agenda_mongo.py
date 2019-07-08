from flask import Flask, request, redirect, render_template

from model_mongo import *

app = Flask(__name__)


@app.route("/incluir", methods =["POST", "GET"])
def pag_incluir():
    titulo= "Curso Python - Formulario"
    if "msg" in request.args:
        msg = request.args["msg"]
    else:
        msg = ""
    return render_template("agenda_incluir.html", titulo=titulo, msg=msg)

@app.route("/gravar", methods =["POST", "GET"])
def pag_grava_agenda():
    titulo= "Curso Python - Trata"
    if request.method == "POST":
        data = request.form
        nome = data["nome"]
        tel = data["telefone"]
    else:
        nome = request.args["nome"]
        tel = request.args["telefone"]

    ag1 = minha_agenda()
    if ag1.write_contato({"nome": nome, "tel": tel}):
        pag_ret = "/"
    else:
        pag_ret = "/agenda_incluir?msg='O contato {} existe na agenda'".format(nome)
    return redirect(pag_ret)

@app.route("/")
def pag_agenda():
    titulo = "Curso Python - Agenda"
    ag1 = minha_agenda()
    dic_agenda = ag1.get_agenda()

    # Ordenar  nomes
    lista_nomes = list(dic_agenda.keys())
    lista_nomes.sort()
    tabela = []
    return render_template("agenda.html", titulo=titulo, lista_nomes=lista_nomes, dic_agenda=dic_agenda)

@app.route("/apaga/<nome>")
def pag_apaga(nome):
    titulo = "Curso Python - Agenda"
    ag1 = minha_agenda()
    ag1.delete_contato(nome)

    return redirect("/")


if __name__ == "__main__":
    app.run(port=8080, debug=True)




