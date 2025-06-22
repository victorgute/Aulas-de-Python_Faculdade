print("Insira 4 digitos inteiros: ")
numeros = int(input())

mil = int(numeros / 1000)

resto = int(numeros % 1000)

print("Insira 4 digitos: ", numeros)
print("Valor em milhar: ", mil)
print("Resto do valor em milhar: ", resto)


centerna = int(resto / 100)

resto = int(resto % 100)

print("Valor em centena: ", centerna)
print("Resto do valor em centena: ", resto)


dezena = int(resto / 10)

resto = int(resto%10)

print("Valor em dezena: ", dezena)
print("Resto do valor em dezena: ", resto)

unidade = int(resto / 1)

resto = int(resto % 1)
print("Valor em unidade: ", unidade)


soma = int((unidade*1000)  + (dezena*100) + (centerna*10) + (mil*1))
print("Seu resultado na ordem inversa é: ", soma)

