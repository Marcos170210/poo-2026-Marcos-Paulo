class Pessoa:
    def __init__(self, nome, cpf, mensalidade_base):
        self._nome = nome
        self._cpf = cpf
        self._mensalidade_base = mensalidade_base

    def calcular_pagamento(self):
        return self._mensalidade_base


class Aluno(Pessoa):
    def __init__(self, nome, cpf, mensalidade_base, nota_desempenho):
        super().__init__(nome, cpf, mensalidade_base)
        self._nota_desempenho = nota_desempenho


    def calcular_pagamento(self):
        if self._nota_desempenho >= 9.0:
            return self._mensalidade_base * 0.80

        return self._mensalidade_base


class Professor(Pessoa):
    def __init__(self, nome, cpf, mensalidade_base, horas_extras):
        super().__init__(nome, cpf, mensalidade_base)
        self._horas_extras = horas_extras


    def calcular_pagamento(self):
        return self._mensalidade_base + (self._horas_extras * 40.00)




def exibir_relatorio_financeiro(pessoa):
    print("\n========== RELATÓRIO FINANCEIRO ==========")
    print(f"Nome: {pessoa._nome}")
    print(f"CPF: {pessoa._cpf}")
    print(f"Valor final: R$ {pessoa.calcular_pagamento():.2f}")
    print("===========================================")




def ler_float_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))

            if valor <= 0:
                print("Erro: digite um valor maior que zero.")
                continue

            return valor

        except ValueError:
            print("Erro: digite um número válido.")


def ler_int_nao_negativo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))

            if valor < 0:
                print("Erro: digite um número inteiro maior ou igual a zero.")
                continue

            return valor

        except ValueError:
            print("Erro: digite um número inteiro válido.")




def main():
    print("===== SISTEMA ACADÊMICO =====")

    nome = input("Nome: ")
    cpf = input("CPF: ")
    mensalidade = ler_float_positivo("Mensalidade base: ")

    print("\nEscolha o tipo de usuário:")
    print("1 - Aluno")
    print("2 - Professor")

    while True:
        try:
            opcao = int(input("Digite a opção: "))

            if opcao not in (1, 2):
                print("Erro: escolha 1 ou 2.")
                continue

            break

        except ValueError:
            print("Erro: digite apenas 1 ou 2.")

    if opcao == 1:
        nota = ler_float_positivo("Nota de desempenho: ")
        pessoa = Aluno(nome, cpf, mensalidade, nota)

    else:
        horas_extras = ler_int_nao_negativo("Horas extras trabalhadas: ")
        pessoa = Professor(nome, cpf, mensalidade, horas_extras)

    try:
        exibir_relatorio_financeiro(pessoa)
        print("\nRelatório financeiro gerado com sucesso!")

    except Exception as erro:
        print(f"\nOcorreu um erro ao gerar o relatório: {erro}")

    finally:
        print("Processamento do relatório encerrado.")


if __name__ == "__main__":
    main()
