soma = 0
for const in range(10):
    altura = float(input(("Insira uma altura: ")))
    soma = soma + altura
    print(soma)

media = soma / 10

print(f"Essa é a media: {media:.2f}")
