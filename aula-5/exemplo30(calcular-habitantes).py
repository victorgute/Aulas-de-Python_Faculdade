import random as rd
soma = 0
idades = 0
contagem = 0
contagemfilhos = 0
somafilhos = 0
quantidadehomens = 0
velho = 0
rendavelho = 0
maisrenda = 0
rendamulher = 0
generos = ["Homem", "Mulher"]


for habitantes in range(2000):
    idade = rd.randint(18,100)
    renda = rd.randint(1500,10000)
    genero = rd.choice(generos)
    filhos = rd.randint(0,7)
    soma = renda + soma
    somafilhos = somafilhos + filhos
    if filhos > 3: idades = idades + idade
    if filhos > 3: contagem = contagem + 1
    if filhos > 0: contagemfilhos = contagemfilhos + 1
    if genero == "Homem" and idade < 30:  quantidadehomens = quantidadehomens + 1
    if genero == "Homem" and idade > velho: velho = idade
    if idade > velho: rendavelho = renda
    if genero == "Mulher" and renda > maisrenda: maisrenda = renda
    if renda > maisrenda: rendamulher = idade

# 1 - Renda media (2000)
rendamedia = renda % 2000
# print(rendamedia, soma)

# 2 - Media de idade para mais de 3 filhos
filhosmedia = idades // contagem
# print(filhosmedia, idades, contagem)

# 3 - Quantidade de homens com menos de 30 anos 
quantidadehomens
# print(quantidadehomens)

# 4 - Média de numeros de filhos
mediafilhos = somafilhos // contagemfilhos
# print(mediafilhos, somafilhos, contagemfilhos)

# 5 - Renda do homem mais velho
rendavelho
# print(velho, rendavelho)

# 6 - Idade da mulher com mais renda
rendamulher
# print(rendamulher,maisrenda )


print(f"A) Renda media: {rendamedia}")
print(f"B) Media de idade para mais de 3 filhos: {filhosmedia}")
print(f"C) Quantidade de homens com menos de 30 anos: {quantidadehomens}")
print(f"D) Média de numeros de filhos: {mediafilhos}")
print(f"E) Renda do homem mais velho: Renda: {rendavelho} Idade: {velho}")
print(f"F) Idade da mulher com mais renda: Idade: {rendamulher} Renda: {maisrenda}")