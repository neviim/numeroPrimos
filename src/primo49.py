# -*- coding: utf-8 -*-
# Neviim - 2018
# V-0.1.0

# Uma curiosidade que tive, saber quantas vezes os numeros de 0 a 9 se repetem
# no ultimo numero primo encontrado.

arquivo = open("../data/M74207281.txt","r")
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
Numero de digitos a processar: 22.338.618

Matrix: {'0': 2233259, '1': 2233437, '2': 2234193, '3': 2232135, '4': 2232328, '5': 2236279, '6': 2234254, '7': 2233628, '8': 2234257, '9': 2234848, 'digitos': 22338618}

Matrix: {'0': 2233259,
         '1': 2233437,
         '2': 2234193,
         '3': 2232135,
         '4': 2232328,
         '5': 2236279,
         '6': 2234254,
         '7': 2233628,
         '8': 2234257,
         '9': 2234848,
   'digitos': 22338618}

'''

validaSoma(sm)
print("Matrix: "+ str(sm))

arquivo.close()
