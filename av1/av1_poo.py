class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base

    def get_salario_base(self):
        return self.__salario_base

    def set_salario_base(self, novo_salario):
        if novo_salario > 0:
            self.__salario_base = novo_salario
        else:
            print("O salário deve ser maior que zero.")

    def calcular_salario_final(self):
        return self.__salario_base


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base, bonus_gestao):
        super().__init__(nome, matricula, salario_base)
        self.bonus_gestao = bonus_gestao

    def calcular_salario_final(self):
        return self.get_salario_base() + self.bonus_gestao


class Desenvolvedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, nivel):
        super().__init__(nome, matricula, salario_base)
        self.nivel = nivel

    def calcular_salario_final(self):
        if self.nivel == "Senior":
            return self.get_salario_base() + 1500
        else:
            return self.get_salario_base()



gerente = Gerente(
    "Carlos",
    "G001",
    8000,
    2000
)

desenvolvedor = Desenvolvedor(
    "Marcos",
    "D001",
    6000,
    "Senior"
)

gerente.__salario_base = -100

print("Salário base do gerente:", gerente.get_salario_base())
print("Salário final do gerente:", gerente.calcular_salario_final())

print("Salário base do desenvolvedor:", desenvolvedor.get_salario_base())
print("Salário final do desenvolvedor:", desenvolvedor.calcular_salario_final())