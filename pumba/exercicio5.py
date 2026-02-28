#Conversão de Tempo:
segundos = int(input("Informe o tempo em segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{horas} hora(s), {minutos} minuto(s) e {segundos_restantes} segundo(s)")
