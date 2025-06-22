print("Coloque o valor da nota: ")
nota = int(input())

if nota<0 or nota>10 :
    print("Nota inválida")
    print("Nota deve estar no intervalo de [0;10]")
else:
    if nota>=9 and nota<=10 : print("Nota: A")
    if nota>=7 and nota<=8 : print("Nota: B")
    if nota>=5 and nota<=6 : print("Nota: C")
    if nota>=3 and nota<=4 : print("Nota: D")
    if nota>=0 and nota<3 : print("Nota: E")