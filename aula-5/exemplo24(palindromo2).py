texto = input("Digite uma palavra: ")

if texto != texto[::-1]:
    print("A palavra não é um palíndromo")
else:
    print("A palavra é um palíndromo")