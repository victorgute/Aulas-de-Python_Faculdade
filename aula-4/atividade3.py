peso = float(input("Coloque o seu peso: "))
altura = float(input("Coloque a sua altura: "))

imc = peso / altura**2
print("Seu IMC: ", imc)

if imc < 18.6: print("Abaixo do peso")
elif imc < 24.9: print("Peso ideal")
elif imc < 29.9: print("Sobre-peso")
elif imc < 34.9: print("Obessidade grau 1")
elif imc < 39.9: print("Obessidade grau 2")
else: print("Obessidade grau 3")
