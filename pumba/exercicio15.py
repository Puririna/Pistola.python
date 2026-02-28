#Alistamento militar:
sexo = input("Informe seu sexo (M/F): ").upper()
idade = int(input("Informe sua idade: "))
if sexo == "M" and idade >= 18:
    print("Você deve se alistar.")
else:
    print("Você não precisa se alistar.")
