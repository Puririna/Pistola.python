''
estoque = []

while True:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))

    produto = {"nome": nome, "preco": preco}

    estoque.append(produto)

    continuar = input("Deseja adicionar outro produto? (s/n): ").lower()
    if continuar == "n":
        break

print("\n--- Estoque Final ---")
valor_total = 0
for i, item in enumerate(estoque, start=1):
    print(f"{i}. {item['nome']} - R$ {item['preco']:.2f}") 
    valor_total += item['preco']

print(f"\nValor total do estoque: R$ {valor_total:.2f}")
