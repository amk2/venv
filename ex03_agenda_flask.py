"""
requests and upload

"""

from flask import Flask, request, redirect
app = Flask(__name__)

template1 = open("index.html").read()
template2 = open("pag2.html").read()
template3 = open("agenda.html").read()
template4 = open("agenda_incluir.html").read()
template5 = open("agenda_apagar.html").read()


bloco2 = """
      <form action = "http://localhost:5000/upload" method = "POST"
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>
"""



"""
Exemplo de chamada POST
curl http://127.0.0.1:5000/trata -d "num1=1&num2=2"

url_for('static', filename='style.css')

"""
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
    return template4.format(titulo=titulo, msg=msg)

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
        pag_ret = "/incluir?msg='O contato {} existe na agenda'".format(nome)
    return redirect(pag_ret)

@app.route("/")
def pag_agenda():
    titulo = "Curso Python - Agenda"
    dic_agenda = carrega_agenda()
    # Ordenar  nomes
    lista_nomes = list(dic_agenda.keys())
    lista_nomes.sort()
    tabela = []
    for x in lista_nomes:
        tabela.append("""<tr> 
                        <td> {} </td>
                        <td>{}</td>
                        <td><a href='/apaga/{}'>del</a> </td> 
                       </tr>""".format(x, dic_agenda[x],x))
    tabela_completa = """
    <table>
    <tr>
       <th>Nome</th>
       <th>Telefone</th>
       <th></th>
    </tr>
    {}
    </table>
    """.format((" ").join(tabela))

    return template3.format(titulo=titulo, tabela_completa=tabela_completa)

@app.route("/apaga/<nome>")
def pag_apaga(nome):
    titulo = "Curso Python - Agenda"
    dic_agenda = carrega_agenda()
    if nome in dic_agenda.keys():
        dic_agenda.pop(nome)
        #del(dic_agenda[nome])
        grava_agenda(dic_agenda)
        tabela_completa = "{} foi apagado".format(nome)
    else:
        tabela_completa = "{} não existe".format(nome)

    return redirect("/")
    #return template3.format(titulo=titulo, tabela_completa=tabela_completa)




@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('{}'.format(f.filename))
    titulo = "Curso Python - Upload"
    bloco = "<p> Upload realizado </p>"
    return template.format(titulo=titulo, bloco= bloco)



if __name__ == "__main__":
    app.run(port=1234, debug=True)






"""

@app.route("/trata", methods =["POST", "GET"])
def pag_trata():
    titulo= "Curso Python - Trata"
    if request.method == "POST":
        data = request.form
        num1 = int(data["num1"])
        num2 = int(data["num2"])
    else:
        num1 = int(request.args["num1"])
        num2 = int(request.args["num2"])
    total = num1 + num2

    bloco = bloco1.format(num1=num1, num2=num2, total=total)
    return template.format(titulo=titulo, bloco= bloco)
"""

