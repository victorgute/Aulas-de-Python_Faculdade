import math

for num in range(1,51):
    #{num:6} = No minimo 6 digitos
    #{math.sqrt(num):.3f} = tres digitos decimais
    print(f"{num:6}: {math.sqrt(num):.3f}")