prova1 = int(input("Valor da prova 1: "))
prova2 = int(input("Valor da prova 2: "))
prova3 = int(input("Valor da prova 3: "))
frequencia = int(input("Valor de frequencia: "))

media = (prova1 + prova2 + prova3)// 3

if frequencia <0 or frequencia>100 : print("Valor de frequencia invalido")
else: 
    if frequencia < 75: print("Reprovado por falta")
    else:
        if frequencia >= 75: acima = frequencia
        if media >= 7 : print("Aprovado em G1")
        else: 
            if media < 4 : print ("Reprovado")
            else: print("Faça o exame G2")
            media2 = int(input("Coloque o valor do exame G2: "))
            media2 = (media + media2) // 2
            if media2 >= 5: print("Aprovado em G2") 
            else: print("Reprovado em G2")