valor1 = int(input("Coloque o primeiro valor: "))
valor2 = int(input("Coloque o segundo valor: "))
valor3 = int(input("Coloque o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3: primeiro = valor1
elif valor1 < valor2 and valor2 > valor3 : primeiro = valor2
else : primeiro = valor3

if valor1 < valor2 and valor1 < valor3: terceiro = valor1
elif valor2 < valor1 and valor2 < valor3: terceiro = valor2
else: terceiro = valor3

if valor1 < primeiro and valor1 > terceiro : segundo = valor1
elif valor2 < primeiro and valor2 > terceiro : segundo = valor2
else: segundo = valor3

print("Ordem cresente dos numeros é: ", terceiro, segundo, primeiro)  
print("Ordem decrescente dos numeros é: ", primeiro, segundo, terceiro)