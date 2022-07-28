VETcodigosProdutos = []
VETestoque = []
j = 0
for i in range(10):
    codigo_produto = int(input(f'\n Digite o código do {i+1}º produto: '))
    VETcodigosProdutos.append(codigo_produto)
    quantidadeProduto = int(input(f'Informe a quantidade do {i+1}º produto: '))
    VETestoque.append(quantidadeProduto)
cliente = int(input('Digite o código do cliente: '))
while cliente > 0:
    codigo_produto = int(input('Qual produto você deseja? '))
    for i in VETcodigosProdutos:
        if codigo_produto == i:
            produto = True
            print('PRODUTO ENCONTRADO!')
        else:
            print('Código Inexistente!')
            j = i
        if produto == True: 
            quantidade_desejada = int(input('Qual a quantidade desejada do produto: '))
            if quantidade_desejada <= VETestoque[j]:
                VETestoque[j] = VETestoque[j] - quantidade_desejada
                print('Pedido atendido! Volte Sempre!')
            else:
                print('Não temos estoque suficiente dessa mercadoria!')
        else:
            print('CÓDIGO INEXISTENTE!')
print('Para sair digite 0.')
