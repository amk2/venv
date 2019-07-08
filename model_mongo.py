from pymongo import MongoClient


class minha_agenda():
    """
    Agenda
    """
    def __init__(self):
        self.banco = MongoClient('localhost', 27017)
        self.db = self.banco["treinamento"]
        self.agenda = self.db["agenda"]

    def get_agenda(self):
        dic_cursor = self.agenda.find()
        dic_agenda = {}
        for item in dic_cursor:
                dic_agenda[item["nome"]] = item["tel"]

        return dic_agenda

    def get_contato(self,nome):
        dic_contato = self.agenda.find_one({"nome": nome})
        return dic_contato

    def write_contato(self, dic_contato):
        dic_existe = self.agenda.find_one({"nome": dic_contato["nome"]})
        if dic_existe :
            ret =  False
        else:
            self.agenda.insert_one(dic_contato)
            ret = True
        return ret

    def delete_contato(self, nome):
        ret = self.agenda.delete_one({"nome":nome})
        return ret.raw_result



if __name__ == "__main__":
    agenda1 = minha_agenda()
    dic_contato_novo = {"nome": "Luiz", "tel": "4444"}
    if agenda1.write_contato(dic_contato_novo):
        print("Gravou")
    else:
        print("Já existe")
    dic_agenda = agenda1.get_agenda()
    for item in dic_agenda:
        print("Nome: {} tel: {}".format(item["nome"], item["tel"]))
    dic_meuContato = agenda1.get_contato("Maria")
    print("O telefone é {}".format(dic_meuContato["tel"]))
    print(agenda1.delete_contato("Luiz"))


