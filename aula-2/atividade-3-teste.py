import math

print("Tempo em segundos: ")
tempo_segundos = int(input())

print("Tempo em horas: ")
tempo_horas = (tempo_segundos // 60) // 60
print(tempo_horas)

print("Tempo em minutos: ")
tempo_minutos = (tempo_segundos // 60)
print(tempo_minutos)

print("Tempo em segundos: ")
tempo_segundo = int(tempo_minutos * 60)
print(tempo_segundo)