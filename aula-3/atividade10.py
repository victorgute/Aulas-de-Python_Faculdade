saldo = float(input("Coloque o saldo medio da sua conta: "))

if saldo <500 : print("Não a limire para seu saldo medio")
if saldo >=500 and saldo <1000 : limite = saldo * 0.08
if saldo >=1000 : limite = saldo * 0.15

print("Seu limite: ", limite)