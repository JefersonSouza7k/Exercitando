custo_transporte = []
produtos = []
lojas = []
custoFinal = []
for i in range(3): #Laço para ciar vetor dos 3 produtos
    produtos.append(input('Produto: '))
for i in range(2): #Loop das lojas
    linha = []
    for j in range(3): #Loop dos preços
        print('-'*10)
        print(f'PRODUTO {j} DA LOJA {i}')
        linha.append(float(input('Preço: R$ ')))
    lojas.append(linha)
print(lojas)
for i in range(3): #laço para criar vetor com custo do transporte dos produtos
    custo_transporte.append(float(input('Custo >> R$')))

for i in range(2):
    linha = [] #linha para a matriz custoFinal
    for j in range(3):
        if lojas[i][j] <= 50:
            imposto = lojas[i][j] * 0.05
        elif lojas[i][j] > 50 and lojas[i][j] <= 100:
            imposto = lojas[i][j] * 0.1
        else:
            imposto = lojas[i][j] * 0.2
        linha.append(lojas[i][j] + custo_transporte[j] + imposto)
    custoFinal.append(linha)
print(custoFinal)
for i in range(2):
    for j in range(3):
        print('-'*20)
        print(f'\n Produto >> {produtos[j]}. \n Loja >> {i}. \n Imposto ?????. \n Custo de transporte >> {custo_transporte[j]}. \n Preço inicial >> {lojas[i][j]}. \n Preço final >> {custoFinal[i][j]}')