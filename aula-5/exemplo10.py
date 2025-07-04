import random

soma = 0
maior = 0
for const in range(10):
    altura = random.uniform(1.5, 2.10)
    soma = soma + altura
    if altura > maior: maior = altura
    print(f"{altura:.2f}")

media = soma / 10



print(f"Essa é a media: {media:.2f}")
print(f"Maior altura: {maior:.2f}")