numero = 1
acumulador = 0
primos = 0
lista_primos = []

while numero <= 100:
    print(f"Divisores de {numero}:")
    divisor = 1
    while divisor <= numero:
        if numero % divisor == 0:
            print(divisor)
            acumulador += 1
        divisor += 1
    print(f"Total de divisores: {acumulador}")
    if acumulador == 2:
        lista_primos.append(numero)
        print("Esse divisor é primo")
    print("-----")
    acumulador = 0
    numero += 1
print(f"Todos os numeros primos: {lista_primos}")