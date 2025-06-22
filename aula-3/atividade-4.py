digitos = int(input("Insira 4 digitos: "))
if digitos < 1111 or digitos > 9999: print("Digitos invalidos, tente novamente")
else :
    mil = digitos // 1000
    resto = digitos % 1000

    centena = resto // 100
    resto = resto % 100

    dezena = resto // 10
    resto = resto % 10

    unidade = resto // 1

    soma = unidade* 1000 + dezena * 100 + centena * 10 + mil * 1

print("Valor invertido : ", soma)

if soma == digitos: print("O número é capicua")
else: print("O número não é capicua")
