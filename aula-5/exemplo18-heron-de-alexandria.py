numero = int(input("Coloque um numero: "))
total = int(input("Quantidade de repetições: "))

aproximacao = 1

for cont in range(1, total+1): #Repete "total" de vezes
    aproximacao = (aproximacao + numero / aproximacao) /2
    print(f"{cont:3}: {aproximacao:.5f}")

print(f"Raiz aproximada: {aproximacao:.5f}")


