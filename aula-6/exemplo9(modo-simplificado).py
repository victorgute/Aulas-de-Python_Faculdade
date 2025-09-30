# 1. Inicialização das variáveis
numero_atual = 1
lista_de_primos = []

# 2. Loop principal para verificar cada número de 1 a 100
while numero_atual <= 100:
    
    divisor_teste = 1
    contador_de_divisores = 0

    # Loop interno para contar os divisores do numero_atual
    while divisor_teste <= numero_atual:
        if numero_atual % divisor_teste == 0:
            contador_de_divisores += 1
        divisor_teste += 1

    # Após testar todos os divisores, verifica se o número é primo
    if contador_de_divisores == 2:
        lista_de_primos.append(numero_atual)

    numero_atual += 1 # Avança para o próximo número

# 3. Exibe o resultado final, uma única vez
print("Análise completa!")
print(f"Os números primos entre 1 e 100 são: {lista_de_primos}")