# Repete a varialvel ate o valor ser um numero natural
valor1 = int(input("Coloque o primeiro valor: "))
while valor1 < 0:
    print("O valor inserido deve ser um numero natural!")
    valor1 = int(input("Insira novamente o primeiro valor: "))

valor2 = int(input("Coloque o segundo valor: "))
while valor2 < 0:
    print("O valor inserido deve ser um numero natural!")
    valor2 = int(input("Insira novamente o segundo valor: "))

# Verifica qual é o maior numero
if valor1 > valor2: maior = valor1
else: maior = valor2

# Verifica qual é o menor numero
if maior > valor1: menor = valor1
else: menor = valor2

# Verifica todos os numeros impares entre o meno e o maior e soma eles
soma = 0
while menor <= maior:
    if  menor % 2 == 1: 
        soma = soma + menor
        print(menor)
    menor = menor + 1

print("Essa é a soma dos valores impares: ", soma)