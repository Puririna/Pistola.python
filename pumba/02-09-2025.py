#Atividade prática
class ProdutoEletronico:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco *= (1 - percentual / 100)

    def __str__(self):
        return f"{self.nome}: R$ {self.preco:.2f}"


class Smartphone(ProdutoEletronico):
    def aplicar_desconto(self, percentual):
        super().aplicar_desconto(percentual + 5)


class Televisor(ProdutoEletronico):
    def aplicar_desconto(self, percentual):
        super().aplicar_desconto(percentual + 10)



estoque = [
    Smartphone("Galaxy S25", 5000.0),
    ProdutoEletronico("Notebook X", 3500.0),
    Televisor("Smart TV 55″", 4500.0),
]

for produto in estoque:
    produto.aplicar_desconto(10)
    print(produto)
