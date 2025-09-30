valor = int(input("Insira um valor: "))
soma_divisores = 0
contagem = 1

while contagem < valor:
    if valor % contagem == 0:
        soma_divisores += contagem
    contagem += 1

if soma_divisores == valor:
    print(f"{valor} é um número perfeito!")
else:
    print(f"{valor} não é um número perfeito.")