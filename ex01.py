# -*- coding: UTF-8 -*-
"""
 ex01.py
 --------

 Exercicio Curso de python - Serpro
 Dada uma lista com 5 alunos e duas outras listas com as notas da
 primeira prova e da segunda , calcule a média e imprima quem  ficou
 em prova final por ter media inferior a 60,  indicando o nome e a
 media obtida

  Data : 23.10.18

"""
alunos = ["Juca", "Roberta", "Maria", "Claudia", "Manuel"]
notaP1 = [60, 70, 40, 90, 50]
notaP2 = [60, 40, 80, 60, 70]

def cadastrar_total_notas(nome_aluno, *notas):
    nota_total = 0
    for nn in notas:
        nota_total = nota_total + nn
    return nota_total
cadastrar_total_notas("jose", 10, 20)

def verifica_aluno(lista_aluno, lista_p1, lista_p2):
    """
    ==========================================
    Teste
    ..........................................
     blablabla
# -*- coding: UTF-8 -*-

     data: xx/xx/xx

    ==========================================
    """
    for x, y, z  in zip(alunos, notaP1, notaP2):
        nota_final = (y +z) /2
        if nota_final <= 59:
            print ("%s ficou para a final com %s de media" % (x, nota_final))
        else:
            print ("%s media:%s" % (x, nota_final))
