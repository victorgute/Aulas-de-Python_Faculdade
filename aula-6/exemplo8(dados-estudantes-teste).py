import random as rd
generos = ["Masculino","Feminino"]
media = 0
contadorMenina = 0
altMediaFem = 0
contadorIdade = 0
alunoVelho = 0
altMaisVelho = 0

# Dados dos estudantes e calculos
for estudantes in range(11):
    idade = rd.randint(18, 30)
    altura = rd.randint(140, 190)
    genero = rd.choice(generos)
    media = media + idade
    if genero == "Feminino": contadorMenina += 1
    if genero == "Feminino": altMediaFem += altura
    if idade > 20: contadorIdade += 1
    if alunoVelho < idade: 
        alunoVelho = idade
        altMaisVelho = altura


# A) Media de idade dos estudantes
media = media // 10
print("Media de idade dos estudantes: ", media)

# B) Media de altura das meninas
altMediaFem = altMediaFem // contadorMenina
print("Media de altura das meninas:", altMediaFem)

# C) Percentual de estudantes com mais de 20 anos
contadorIdade = contadorIdade % estudantes
print("Percentual de estudantes com mais de 20 anos: ", contadorIdade)

# D) Altura dos estudantes mais velhos
print("Altura dos estudantes mais velhos: ", altMaisVelho)