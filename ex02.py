# Sistema de estoque

zerados = 0      
soma = 0         
cont = 0         

while True:
    qtd = int(input("Digite a quantidade em estoque (ou -1 para parar): "))

    if qtd == -1:
        break  # sai do loop

    if qtd == 0:
        zerados = zerados + 1
    else:
        soma = soma + qtd
        cont = cont + 1

# Exibe resultados
print("Produtos zerados:", zerados)

if cont > 0:
    media = soma / cont
    print("Média do estoque:", media)
else:
    print("Não há produtos com estoque diferente de zero.")
