import random

jogador = input("Escolha pedra, papel ou tesoura? ")

computador = random.choice(["pedra", "papel", "tesoura"])
print(f"Computador escolheu: {computador}")

if jogador == "pedra" and computador == "tesoura" : print("Jogador Venceu!")
elif jogador == "tesoura" and computador == "papel": print("Jogador Venceu!")
elif jogador == "papel" and computador == "pedra": print("Jogador Venceu!")
elif computador == "pedra" and jogador == "tesoura" : print("Computador Venceu!")
elif computador == "tesoura" and jogador == "papel" : print("Computador Venceu!")
elif computador == "papel" and jogador == "pedra" : print("Computador Venceu!")
else: print("Empate!!!")