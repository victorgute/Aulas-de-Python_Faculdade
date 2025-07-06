texto = input("Digite uma frase: ")
# Variavel para acumular as contagens
contagem = 0
# Lista com as vogais
vogais = ["a","e","i","o","u"]

# Verifiacar cada item dentro da frase escrita
for letras in texto:
    # Verifica cada vogal com o item da frase
    for vogal in vogais:
        # Faz a comparação com o item da frase com as vogais
        if letras == vogal: contagem = contagem + 1

# Quantidade de vogais
print(contagem)