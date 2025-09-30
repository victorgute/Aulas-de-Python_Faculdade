valor = int(input("Informe um valor: "))
cont = 0
d = 1

while d <= valor:
    if valor % d == 0: cont = cont + 1
    d = d + 1

if cont == 2: print(valor,"é primo")
else: print(valor,"não é primo")