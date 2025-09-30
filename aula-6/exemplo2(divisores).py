valor = int(input("Informe um valor natural: "))
d = 1

while d < valor:
    if valor % d == 0:print(d, "divide", valor)
    d = d + 1