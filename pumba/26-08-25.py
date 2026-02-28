class ProdutoEletronico:
    def __init__(self, nome, preco, marca):
        self.nome = nome
        self.preco = preco
        self.marca = marca

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Marca: {self.marca}")

# Subclasse Tablet que herda de ProdutoEletronico
class Tablet(ProdutoEletronico):
    def __init__(self, nome, preco, marca, possui_caneta):
        super().__init__(nome, preco, marca)
        self.possui_caneta = possui_caneta

    def exibir_informacoes(self):
        super().exibir_informacoes()
        caneta_status = "Sim" if self.possui_caneta else "Não"
        print(f"Possui caneta: {caneta_status}")

# Criando uma instância de Tablet
tablet = Tablet("Galaxy Tab S8", 3499.99, "Samsung", True)

# Adicionando o tablet ao estoque
estoque = [tablet]

# Exibindo as informações do tablet
for produto in estoque:
    produto.exibir_informacoes()

