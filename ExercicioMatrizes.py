matriz = []
for i in range(6):
    linha = []
    for j in range(3):
        numero = int(input('Digite um número: '))
        linha.append(numero)
    matriz.append(linha)
# print(f'A matriz é: {matriz}') para visualizar de forma padrão do sistema
for i in range(6):  # para visualizar em formato próximo a matriz real
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print('')
maior = matriz[i][j]
menor = matriz[i][j]
for i in range(6):
    for j in range(3):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        else:
            if matriz[i][j] < menor:
                menor = matriz[i][j]
print('-'*30)
print(f'\n O MAIOR valor foi {maior} na(s) posição(ões): ', end='')
for i in range(6):
    for j in range(3):
        if matriz[i][j] == maior:
            print(f'Linha {i} e coluna {j}')
print(f'\n O MENOR valor foi {menor} na(s) posição(ões): ', end='')
for i in range(6):
    for j in range(3):
        if matriz[i][j] == menor:
            print(f'Linha {i} e coluna {j}')
