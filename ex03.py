total = 0       
soma = 0        
satisfeitos = 0 
while True:
    nota = int(input("Digite a nota de satisfação (1 a 5, ou 0 para encerrar): "))

    if nota == 0:
        break  # sai do loop

    if nota >= 1 and nota <= 5:
        total = total + 1
        soma = soma + nota

        if nota >= 4:
            satisfeitos = satisfeitos + 1
    else:
        print("Nota inválida, digite entre 1 e 5 ou 0 para sair.")

# Resultados
print("Quantidade total de respostas:", total)

if total > 0:
    media = soma / total
    print("Média de satisfação:", media)
else:
    print("Não houve respostas.")

print("Clientes satisfeitos (nota 4 ou 5):", satisfeitos)
