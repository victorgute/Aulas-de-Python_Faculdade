print("Coloque o valo do evento em segundos: ")
event_seconds = int(input())

tempo_horas = print("Valor em horas: ", int(event_seconds / 3600))

resto = event_seconds%3600
minutos = int(resto // 60)
segundos = resto % 60

tempo_minutos = print("Valor em minutos: ", int(minutos))

tempo_segundos = print("Valor em segundos: ", int(segundos))

