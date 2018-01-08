# -*- coding: utf-8 -*-
# Neviim - 2018
# V-0.1.0

# Uma curiosidade que tive, saber quantas vezes os numeros de 0 a 9 se repetem
# no ultimo numero primo encontrado.

arquivo = open("../data/M77232917.txt","r")
sm = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "digitos":0}

# valisna soma digitos por linha e os somam
def validaSoma(lista):
    soma = 0
    for x in lista:
        soma += lista[str(x)]
    sm["digitos"] += soma
    return True

# soma repeticao de digitos
for linha in arquivo:
    linha = linha.replace('\n', '')

    for x in linha:
        sm[str(x)] += 1

    #validaSoma(sm)
    #print(".")

'''
Numero de digitos a processar: 23.249.425

Matrix: {'0': 2325846, '1': 2324106, '2': 2323306, '3': 2325845, '4': 2326305,
         '5': 2325065, '6': 2324655, '7': 2324051, '8': 2326039, '9': 2324207, 'digitos': 23249425}

        {
        '0': 2325846,
        '1': 2324106,
        '2': 2323306,
        '3': 2325845,
        '4': 2326305,
        '5': 2325065,
        '6': 2324655,
        '7': 2324051,
        '8': 2326039,
        '9': 2324207,
  'digitos': 23249425}
'''

validaSoma(sm)
print("Matrix: "+ str(sm))

arquivo.close()
