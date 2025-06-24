mes = int(input("Insira um mes: "))
ano = int(input("Insira um ano:"))

if mes <1 or mes >12: print("Mês invalido")
else:
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0: biseexto = 0
    else: biseexto = 1
    if mes == 2 and biseexto == 0: dias = 29
    elif mes == 2 and biseexto == 1: dias = 28
    else:
        if mes  == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: dias = 31
        else: dias = 30

print(f"Mês {mes} do anos {ano} tem {dias} dias")