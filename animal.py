# Classe base Empregado
class Empregado:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_b0ase = salario_base

    def calcular_salario(self):
        return self.salario_base

# Subclasse Gerente
class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus

# Subclasse Vendedor
class Vendedor(Empregado):
    def __init__(self, nome, salario_base, comissao, vendas):
        super().__init__(nome, salario_base)
        self.comissao = comissao
        self.vendas = vendas

    def calcular_salario(self):
        return self.salario_base + (self.comissao * self.vendas)

# Criando instâncias de Gerente e Vendedor
gerente = Gerente("Alice", 5000, 1000)  # Salário base de 5000 + bônus de 1000
vendedor = Vendedor("Carlos", 3000, 0.1, 50000)  # Salário base de 3000 + 10% de comissão sobre 50000 em vendas

# Calculando e exibindo os salários
print(f"Salário total do gerente {gerente.nome}: R$ {gerente.calcular_salario()}")
print(f"Salário total do vendedor {vendedor.nome}: R$ {vendedor.calcular_salario()}")
