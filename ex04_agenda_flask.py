from flask import Flask, request, redirect, render_template
app = Flask(__name__)

def carrega_agenda():
    agenda = open("agenda.csv").readlines()
    dic_agenda = {}
    for item in agenda:
        print(item)
        if item.find("|"):
            nome, tel = item.split("|")
            dic_agenda[nome] = tel
    return dic_agenda
 

def grava_agenda(dic_agenda):
    arq_agenda = open("agenda.csv", "w")
    for x in dic_agenda:
        arq_agenda.write("{}|{}\n".format(x, dic_agenda[x].strip()))
    arq_agenda.close()


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

    dic_agenda = carrega_agenda()
    if not(nome in dic_agenda.keys()):
        dic_agenda[nome] = tel
        grava_agenda(dic_agenda)
        pag_ret = "/"
    else:
        pag_ret = "/agenda_incluir?msg='O contato {} existe na agenda'".format(nome)
    return redirect(pag_ret)

@app.route("/")
def pag_agenda():
    titulo = "Curso Python - Agenda"
    dic_agenda = carrega_agenda()
    # Ordenar  nomes
    lista_nomes = list(dic_agenda.keys())
    lista_nomes.sort()
    return render_template("agenda.html", titulo=titulo, lista_nomes=lista_nomes, dic_agenda=dic_agenda)

@app.route("/apaga/<nome>")
def pag_apaga(nome):
    titulo = "Curso Python - Agenda"
    dic_agenda = carrega_agenda()
    if nome in dic_agenda.keys():
        dic_agenda.pop(nome)
        grava_agenda(dic_agenda)

    return redirect("/")


if __name__ == "__main__":
    app.run(port=1234, debug=True)




