valor_parcelas = valor_final = 0
quantidade_parcelas = 6
porcentagem = 3
valor_carro = float(input('Informe o valor do carro: R$ '))
print('-'*5, 'TABELA', '-'*5, '\n', 'Parcelas - Preço final - Valor da parcela')
while True:
    if quantidade_parcelas > 60:
        break
    valor_final = valor_carro + (porcentagem / 100 * valor_carro)
    valor_parcelas = valor_final / quantidade_parcelas
    print(quantidade_parcelas, '-', valor_final, '-', valor_parcelas)
    quantidade_parcelas = quantidade_parcelas + 6
    porcentagem = porcentagem + 3
print(f'Valor à vista R$ {valor_carro - (0.20 * valor_carro)} reais.')
