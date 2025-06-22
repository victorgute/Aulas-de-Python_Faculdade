import math

a = int(input("Coloque o valor de a: "))
b = int(input("Coloque o valor de b: "))
c = int(input("Coloque o valor de c: "))

delta = (b**2) - 4*(a*c)
if delta<0 or a ==0 : print("Delta negativo ou divisao por zero")
else:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("x1 e x1 de Baskara: ", x1, x2)