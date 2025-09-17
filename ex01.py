numero_de_vendas = int(input("Digite a quantidade de vendas: "))

total_apurado = 0.0

for i in range(numero_de_vendas):
    valor_da_venda = float(input(f"Insira o valor da venda {i + 1}: R$ "))
    total_apurado += valor_da_venda

print(f"O faturamento total foi de: R$ {total_apurado:.2f}")
