mes = int(input("Escolha um mês (1-12): "))

if mes <1 or mes > 12: print("Numero de mes invalido")
else:
    if mes == 2: dias = 28
    else:
        if mes % 2 == 0: dias = 30
        else: dias = 31
        if mes <= 7 : dias
        else:
            if mes % 2 == 0: dias = 31
            else: dias = 30

print("Quantidade de dias no mês: ", dias)