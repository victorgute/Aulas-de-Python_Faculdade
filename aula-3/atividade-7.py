dia = int(input("Coloque um dia de 1 a 7: "))

if dia <1 or dia >7 :
    print("Dia invalido")
else:
    if dia == 1 : print("Segunda-feira")
    if dia == 2 : print("Terça-feira")
    if dia == 3 : print("Quarta-feira")
    if dia == 4 : print("Quinta-feira")
    if dia == 5 : print("Sexta-feira")
    if dia == 6 : print("Sábado")
    if dia == 7 : print("Domingo")
    print("Dia da semana: ", dia)