funcionarios = []
salarios_liquidos = []

qtd = int(input("Digite a quantidade de funcionários: "))

for i in range(qtd):
    nome = input("Nome do funcionário: ")
    salario = float(input("Salário bruto: "))

    desconto = salario * 0.10
    liquido = salario - desconto

    funcionarios.append(nome)
    salarios_liquidos.append(liquido)

print("\n--- Folha de Pagamento ---")
for i in range(qtd):
    print("Funcionário:", funcionarios[i], "- Salário líquido: R$", round(salarios_liquidos[i], 2))
