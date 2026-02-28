
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        # Bônus padrão de 10%
        return self.salario * 0.1



class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario) 
        self.departamento = departamento

    def calcular_bonus(self):
       
        return (self.salario * 0.15) + 500



class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem_principal):
        super().__init__(nome, salario)
        self.linguagem_principal = linguagem_principal

    def calcular_bonus(self):

        return self.salario * 0.2

if __name__ == "__main__":
    
    funcionario_comum = Funcionario("João", 2000)
    print(f"Bônus do {funcionario_comum.nome}: R${funcionario_comum.calcular_bonus():.2f}")

    gerente_ana = Gerente("Ana", 2000, "Vendas")
    print(f"Bônus da {gerente_ana.nome}: R${gerente_ana.calcular_bonus():.2f}")
