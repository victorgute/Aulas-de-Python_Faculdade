ano = int(input("Insira um ano: "))

if ano % 100 == 0 and ano % 400 == 0 or ano % 4 == 0 and ano % 100 >0: print(f"{ano} é bissexto")
else: print(f"{ano} não é bissexto")