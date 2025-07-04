num = int(input("Valor desejado: "))
total = int(input("Quantidade de repetições: "))

aprox = 1
anterior = 0

for cont in range(1, total +1):
    aprox = (aprox + num/aprox) / 2
    print (f"{cont:3} {aprox:.5f}")
    diferenca = abs(aprox-anterior)
    if diferenca < 0.001:
        break
    anterior = aprox

print(f"Raiz aproximada: {aprox:.5f}")