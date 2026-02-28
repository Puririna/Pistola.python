def recomendacao_conteudo():
    #Usuario
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    if idade.isdigit():
        print("Idade inválida. Por favor, tente novamente.")
        return

    idade = int(idade)

    # Recomendação 
    if idade < 12:
        print(f"Olá, {nome}! Como você tem {idade} anos, recomendamos conteúdo infantil!")
    elif 12 <= idade <= 17:
        print(f"Olá, {nome}! Como você tem {idade} anos, recomendamos jogos e filmes juvenis!")
    elif idade >= 18:
        print(f"Olá, {nome}! Como você tem {idade} anos, recomendamos filmes e livros adultos!")
    else:
        print("Idade inválida.")

#"chamar" funçao
recomendacao_conteudo()