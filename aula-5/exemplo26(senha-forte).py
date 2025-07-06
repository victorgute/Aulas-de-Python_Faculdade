senha = input("Digite sua senha: ")
digitos = "1234567890"
pontuação = "e!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
invalido = False
tamanho = False
numero = False
caractere = False


for geral in senha:
    for caracteres in range(len(senha)):
        if caracteres >=7: invalido = True
    for letras in geral:
        if letras.isupper():
            tamanho = True
    for numeros in geral:
        for digito in digitos:
            if numeros == digito:
                numero = True
    for pontua in geral:
        for ponto in pontuação:
            if pontua == ponto:
                caractere = True

if invalido and tamanho and numero and caractere:
    print("Sua senha é forte")
else:
    print("Sua senha é fraca")