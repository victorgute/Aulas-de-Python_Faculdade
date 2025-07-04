import random

# Variaveis para acumulação
cursos =("Mecânica", "Espacial", "Software", "Elétrica", "Civil", "Ambiental")
nomes = ["Alice", "Bob", "Charlie", "David", "Eve", "Victor", "Pedro", "Matheus"]
soma = 0
maior = 0
quantidade = 0

# Verificação dos 50 alunos
for estudantes in range(50):
    #Valores que cada aluno vai ter
    nome = random.choice(nomes)
    idade = random.randint(20, 70)
    semestre = random.randint(1, 16)
    curso = random.choice(cursos)
    #Soma de todas as idades dos alunos
    soma += idade
    #Separando o nome do aluno mais velho e o curso dele
    if idade > maior: 
        maior = idade
        curso_maior = curso
        nome_maior = nome
    #Verificando a quantidade de alunos que estão no 5 semestres
    if semestre == 5: 
        quantidade = quantidade + 1
    #Valores de cada aluno
    print(idade)
    print(nome)
    print(semestre)
    print(curso)
#Media de idade dos alunos
media = soma // 50

print(f"Media de idade dos alunos: {media}")
print(f"Nome do aluno mais velho: {nome_maior}")
print(f"Idade do aluno mais velho: {maior}")
print(f"Curso do aluno mais velho: {curso_maior}")
print(f"Quantidade de alunos acima do 5 semestre: {quantidade}")