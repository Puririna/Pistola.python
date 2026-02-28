
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if not idade.isdigit():
    print("Idade inválida. Por favor, tente novamente.")
    
idade = int(idade)

if idade < 8:
    print(f"Olá, {nome}! Como você tem {idade} anos, você é muito novo para competir!")
elif 8 <= idade <= 12:
    print(f"Olá, {nome}! Como você tem {idade} anos, você é da categoria infantil!")
elif 13 <= idade <= 17:
    print(f"Olá, {nome}! Como você tem {idade} anos, você é da categoria juvenil!")
elif 18 <= idade <= 30:
    print(f"Olá, {nome}! Como você tem {idade} anos, você é da categoria adulto!")
elif idade > 30:
    print(f"Olá, {nome}! Como você tem {idade} anos, você é da categoria sênior!")
else:
    print("Idade inválida.")
        
sexo = input("Informe seu sexo (M/F): ")
if sexo == "M":
   print(f"Você pertence a categoria masculina, {nome}!")
if sexo == "F":
   print(f"Você pertence a categoria feminina, {nome}!")
   
experiencia = input("Digite quantos anos de experiência você tem: ")

if not experiencia.isdigit():
    print("Resposta invalida. Por favor, tente novamente.")
    
experiencia = int(experiencia)

if experiencia <= 1:
    print(f"Como você tem {experiencia} anos de experiencia, você é iniciante!")
elif 1 <= experiencia <= 3:
    print(f"Como você tem {experiencia} anos de experiencia, você é intermediário/a!")
elif experiencia > 3:
    print(f"Como você tem {experiencia} anos de experiencia, você é avançado/a!")
else:
    print("Resposta inválida.")
   

print(f"Você tem {idade} anos , é da categoria {sexo}, e possui {experiencia} anos de experiencia!")