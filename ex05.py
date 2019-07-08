# -*- coding: UTF8 -*-

def pizzaria(pizza, *ingredientes, **extras):
    """
    Pizzaria
     Calcula o varo final de uma pizza baseado no tipo escolhido e 
     os extras.
     
    entrada : 
       nome da pizza 
       ingredientes - lista com os possiveis ingredientes a adicionar
       extras - definiem a massa, fina ou grossa e a borda, com recheio
                ou não
    saida:
       valor total da pizza
       
    """

    lista_pizza = open("pizzaria.csv").readlines()
    tabela_pizza = {}
    for linha in lista_pizza[2:]:
        item, valor = linha.split("|")
        tabela_pizza[item] = int(valor)


    #print(tabela_pizza)
    
    err = ""
    id_item = ""
    try:
        valor_total = tabela_pizza[pizza]
        for item in ingredientes:
            id_item = item
            valor_total = valor_total + tabela_pizza[item]
        import pdb; pdb.set_trace()    
        for chave in extras:
            id_item = chave
            valor_total = valor_total + tabela_pizza[extras[chave]]
    except KeyError:
        valor_total = -1
        err = "Chave %s inválida" % id_item
    return valor_total, err
    
    
if __name__ == "__main__":
    
    total, erro = pizzaria("calabresa", "queijo", "ovo", massa="massa fina", borda="borda simples")

    if total == -1:
        print ("Erro : item %s não encontrado" % erro)
    else:
        print(40*"=")
        print ("Valor a pagar %s" % total)
        print(40*"=")
