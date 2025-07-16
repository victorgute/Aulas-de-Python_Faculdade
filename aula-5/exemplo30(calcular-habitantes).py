import random as rd
soma = 0
idades = 0
contagem = 0
contagemfilhos = 0
somafilhos = 0
quantidadehomens = 0
velho = 0
maisrenda = 0
generos = ["Homem", "Mulher"]


for habitantes in range(1,2001):
    idade = rd.randint(18,100)
    renda = rd.randint(1500,10000)
    genero = rd.choice(generos)
    filhos = rd.randint(0,6)
    soma = renda + soma
    somafilhos = somafilhos + filhos
    if filhos > 3: idades = idades + idade
    if filhos > 3: contagem = contagem + 1
    if filhos >= 1: contagemfilhos = contagemfilhos + 1
    if genero == "Homem" and idade < 30:  quantidadehomens = quantidadehomens + 1
    if genero == "Homem" and idade > velho: velho = idade
    if genero == "Mulher" and renda > maisrenda: maisrenda = renda

# 1 - Renda media (2000)
rendamedia = renda / 2000

# 2 - Media de idade para mais de 3 filhos
filhosmedia = idades // contagem

# 3 - Quantidade de homens com menos de 30 anos 
quantidadehomens

# 4 - Média de numeros de filhos
mediafilhos = somafilhos // contagemfilhos

# 5 - Renda do homem mais velho
velho

# 6 - Idade da mulher com mais renda
