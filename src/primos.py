# -*- coding: utf-8 -*-
# Neviim - 2018
# V-0.1.0

# Uma curiosidade que tive, saber quantas vezes os numeros de 0 a 9 se repetem
# no ultimo numero primo encontrado.

arquivo = open("../data/M43112609.txt","r")
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

# finaliza operacao
validaSoma(sm)
print("Matrix: "+ str(sm))

arquivo.close()
