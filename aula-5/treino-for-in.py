numero = int(input("Escolha um numero de 1 a 10: "))

if numero < 1 or numero >10: print("Numero invalido!")
else:
    for tabuada in range(1,11):
        multi = numero * tabuada
        print(f"{numero} * {tabuada}: {multi}")