soma = 0
num = int(input("Numero: "))

for cont in range(1,num+1):
    soma = soma + cont
    print((f"{cont}: {soma}"))
print(f"Somatório:{soma}")