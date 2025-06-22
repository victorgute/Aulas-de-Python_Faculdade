num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
num3 = int(input("Informe o terceiro numero: "))

a = num3>1 and num3<= 10
b = num1<1 or num1>10
c = num2>num1 and num2>num3
d = num2%7 == 0
e = num2%num3 == 0 or num3%num2 == 0
f_cambiarra = num1 == num2 == num3 
f = num1 == num2 and num1 == num3
g = num1 == num2 or num1 == num3 or num2 == num3

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)