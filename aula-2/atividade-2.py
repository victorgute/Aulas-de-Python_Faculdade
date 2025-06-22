import math

print("Coloque o primeiro valor: ")
valor1 = int(input())

print("Coloque o segundo valor: ")
valor2 = int(input())

a = valor1 + valor2

b = valor1 - valor2

c = (valor1 + valor2) / 2

d = math.fabs(valor1 - valor2)

e = (valor1 + valor2 + math.fabs(valor1-valor2))/2

f = (valor1 + valor2 - math.fabs(valor1-valor2))/2

print("soma: ",a)
print("diferença: ",b)
print("media: ",c)
print("distancia: ",d)
print("maior numero: ",e)
print("menor numero: ",f)