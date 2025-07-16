import random as rd

sorteio = rd.randint(1,100)
acerto = False
print(sorteio)
numero = print("Você tem 10 chances para acertar o número sorteado")
for resposta in range(1,10+1):
    tentativa = int(input(f"Tentativa {resposta}: Escolha um numero de 1 a 100: "))
    if tentativa > sorteio: print("Seu numero é maior que o numero sorteado, tente denovo")
    if tentativa < sorteio: print("Seu numero é menor que o numero sorteado, tente denovo")
    if tentativa == sorteio: acerto = True
    if acerto == True:
        break

if acerto == True: print("Você acertou o numero sorteado, parabéns")
if acerto == False: print(f"Acabou suas tentativas, esse era o numero sorteado: {sorteio}")
