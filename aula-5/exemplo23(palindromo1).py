texto = input("Digite uma palavra: ")

# Iniciando dif com "False" para fazer uma verificação depois
dif = False
# Verifica letra por letra até a metade da palavra
for pos in range(len(texto)//2):
    # Verifica de as letra iniciais batem com as finais
    if texto[pos] !=  texto[-1-pos]:
        # Verifica se toda a operação funcionou e retorna True
        dif = True
        # Para o codigo quando termina de verficar as letras
        break

# Verificando se "dif" deu True ou False
if dif:
    print("A frase não  é um palíndromo...")
else:
    print("A frase é um palíndromo!")