custo = float(input("Coloque o valor de custo: "))

if custo >=1 and custo < 10 : lucro = custo * 0.7

if custo >= 10 and custo < 30 : lucro = custo * 0.5

if custo >= 30 and custo <50 : lucro = custo * 0.4

if custo >= 50 : lucro = custo * 0.3

venda = custo + lucro

print("Valor de venda: ", venda)

