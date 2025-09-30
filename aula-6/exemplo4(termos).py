nTermos = int(input("Informe a quantidade de termos: "))

if nTermos <= 0: "Numero de termos invalido!"
else:
    soma = 0
    cont = 1
    numerador = 2
    denominador = 1
    while cont <= nTermos:
        soma = soma + 1/cont
        cont = cont + 1
        numerador = numerador + 2
        denominador = denominador + 2
    print("Soma: ", soma)