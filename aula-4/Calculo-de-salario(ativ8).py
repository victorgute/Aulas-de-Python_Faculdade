salario = float(input("Coloque o seu salário bruto: "))
dependentes = int(input("Coloque o numero de dependentes: "))

#Verificação do INSS
if salario <= 1212: inss = salario * 0.075
if salario <= 1212 and inss > 90.9: inss = 90.9
elif salario > 1212 and salario <= 2427.35: inss = (salario * 0.09) - 18.18
if salario > 1212 and salario <= 2427.35 and inss > 200.28: inss = 200.28
elif salario > 2427.35 and salario <= 3641.03: inss = (salario * 0.12) - 91
if salario > 2427.35 and salario <= 3641.03 and inss > 345.92: inss = 345.92
elif salario > 3641.03: inss = (salario * 0.14) - 163.82
if salario > 3641.03 and inss > 828.39: inss = 828.39

#Verificação de IRRF
calculo = salario - inss - (dependentes * 189.59)

if calculo <= 1903.98: irrf = calculo
elif calculo > 1903.98 and calculo <= 2826.65: irrf = (calculo * 0.075) - 142.80 
elif calculo > 2826.65 and calculo <= 3751.05: irrf = (calculo * 0.15) - 142.80
elif calculo > 3751.05 and calculo <= 4664.68: irrf = (calculo * 0.225) - 636.16
elif calculo > 4664.68: irrf = (calculo * 0.275) - 869.36

liquido = salario - inss - irrf

print(f"Seu salario de {salario} tem {inss} de INSS e {irrf} de IRRF e valor liquido fica: {liquido}")