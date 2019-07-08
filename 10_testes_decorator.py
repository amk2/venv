def party():
    """
    Nested function
    """
    print("Estou de fora =[")

    def start_party():
        return "Estamos dentro! Uhullll!"

    def finish_party():
        return 'A festa acabou! =[")'

    print(start_party())
    print(finish_party())

# "Criador" de funções de potência
def cria_potencia(x):
    def potencia(num):
        return x ** num
    return potencia


def decorator(funcao):
    """
    Exemplo de decorator
    """
    def wrapper():
        print ("Estou antes da execução da função passada como argumento")
        funcao()
        print ("Estou depois da execução da função passada como argumento")

    return wrapper

def outra_funcao():
    print ("Sou um belo argumento!")



if __name__ == "__main__":
    #testa o nested function party()
    party()

    input("Resultado da Nested function")

    # Função retonando  funções
    # Potência de 2 e 3
    potencia_2 = cria_potencia(2)
    potencia_3 = cria_potencia(3)

    # Resultado
    print(potencia_2(2))
    print(potencia_3(2))

    input("Resultado da das Funções geradas")


    # testa o decorator
    funcao_decorada = decorator(outra_funcao)
    funcao_decorada()
