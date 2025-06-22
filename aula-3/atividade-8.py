nota1 = int(input("Coloque a primeira nota: "))

nota2 = int(input("Coloque a segunda nota: "))

nota3 = int(input("Coloque a terceira nota: "))


maior = nota1
if maior < nota2 : maior = nota2
if maior <nota3 : maior = nota3

menor = nota1
if menor > nota2 : menor = nota2
if menor > nota3 : menor = nota3

meio = (nota1 + nota2 + nota3) - maior - menor


maior = maior * 5
meio = meio * 2.5
menor = menor * 2.5

media = (maior + meio + menor) // 3

print("Media ponderada: ", media)