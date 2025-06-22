sistolica = int(input("Valor da Sistólica: "))
diastolica = int(input("Valor da Diastólica: "))

if sistolica <120 and diastolica <80: print("Normal")
elif sistolica <129 and diastolica <80: print("Elevada")
elif sistolica <139 and diastolica <89: print("Hipertensão Estágio 1")
elif sistolica <180 and diastolica <120: print("Hipertensão Estágio 2")
elif sistolica >=180 or diastolica >=120: print("Crise Hipertensiva")