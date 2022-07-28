media = cont_idade = quant_pessoas = porcentagem = quantAltura = quantIdade = 0
for i in range(10):
    idade = int(input('Informe a idade: '))
    peso = float(input('Informe o peso da pessoa em quilogramas: Kg '))
    altura = float(input('Digite a altura da pessoa: '))
    print(f'-'*10)
    cont_idade = cont_idade + idade
    media = cont_idade / 10
    if peso > 90 and altura < 1.50:
        quant_pessoas = quant_pessoas + 1
    if idade >= 10 and idade <= 30 and altura > 1.90:
        quantAltura = quantAltura + 1
        porcentagem = (quantAltura * 100) / 10
print(f'\n A média das idades das 10 pessoas é de {media} anos. \n A quantidade de pessoas com peso acima de 90 Kg e altura inferior a 1,50m é de {quant_pessoas} pessoas. \n A porcentagem de pessoas com idade entre 10 e 30 anos e que possuem altura maior que 1,90m é de {porcentagem}%')
''' idade = int(input('Informe a idade: '))
    #peso = float(input('Informe o peso da pessoa em quilogramas: Kg '))
    altura = float(input('Digite a altura da pessoa: '))
    print(f'-'*10)
    cont = cont + 1
    cont_idade = cont_idade + idade
    media = cont_idade / 10
    #if peso > 90 and altura < 1.50:
        #quant_pessoas = quant_pessoas + 1
    if idade >= 10 and idade <= 30 and altura > 1.90:
        quantAltura = quantAltura + 1
        porcentagem = (quantAltura * 100) / 5'''
