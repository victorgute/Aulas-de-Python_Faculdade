horasInicio = int(input("Horario de inicio do jogo em horas: "))
minutosInicio = int(input("Horario de inicio do jogo em minutos: "))

horasFinal = int(input("Horario de término do jogo horas: "))
minutosFinal = int(input("Horario de término do jogo em minutos: "))


horarioInicial = horasInicio *  60 + minutosInicio
horarioFinal = horasFinal * 60 + minutosFinal

if horarioInicial < horarioFinal : duracao = horarioFinal - horarioInicial
else : duracao = 24 * 60 - horarioInicial + horarioFinal

print("Horas: ", duracao // 60)
print("Minutos: ", duracao % 60)
