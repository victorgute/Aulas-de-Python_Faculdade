import math

print("Coloque a sua altura: ")
altura = float(input())

print("Adicione 1 para masculino e 2 para feminino: ")
sexo = int(input())

if sexo == 1:
    peso = (72.7 * altura) - 58
    print("Esse é o seu peso ideal: ", peso)

if sexo == 2:
    peso = (62.1 * altura) - 44.7
    print("Esse é o seu peso ideal: ", peso)

if sexo != 1 and sexo != 2:
    print("Sexo inválido")

