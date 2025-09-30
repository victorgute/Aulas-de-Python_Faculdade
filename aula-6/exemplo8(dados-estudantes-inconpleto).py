cont = 0
soma = 0

while cont < 10:
    print("Cont: ", cont)
    idade = int(input("Informe a idade: "))
    while idade <= 0 or idade >= 60: 
        print("Idade invalidade. Deve estar no intervalo de 0 a 60 anos.")
        idade = int(input("Informe a idade novamente: "))
    
    altura = float(input("Informe a altura: "))
    while altura <= 0 or altura >= 2.1:
        print("Tamanho invalido. Deve estar no intervalo de 0 e 2.1.")
        altura = float(input("Informe a altura novamente: "))

    genero = int(input("Informe o seu genero usando 1 para feminino e 2 para masculino: "))
    while genero != 1 and genero != 2: 
        print("Genero inválido. Deve ser 1 ou 2.")
        genero = int(input("Informe novamente o seu genero usando 1 para feminino e 2 para masculino: "))

    soma = soma + idade
    cont = cont + 1

print("Media de idade dos estudantes: ", soma/cont)
