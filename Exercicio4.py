while True:
    print('\n', '-'*5, 'Menu de Opções', '-'*5,'\n 1. Novo salário \n 2. Férias \n 3. Décimo Terceiro \n 4. Sair \n \n Digite a opção desejada. \n')
    escolha = int(input('Escolha uma das opções acima: '))
    print(f'\n Opção escolhida: {escolha}')
    if escolha == 1:
        salario = float(input('Informe o salário do funcionário: R$ '))
        if salario < 210.00:
            aumento15 = (salario * (15/100) + salario)
            print(f'\n O salário novo do funcionário será de R$ {aumento15} reais, com aumento de 15%.')
        elif salario >= 210.00 and salario <= 600.00:
            aumento10 = (salario * (10/100) + salario)
            print(f'\n O salário novo do funcionário será de R$ {aumento10} reais, com aumento de 10%.')
        elif salario > 600.00:
            aumento5 = (salario * (5/100) + salario)
            print(f'\n O salário novo do funcionário será de R$ {aumento5} reais, com aumento de 5%.')
    if escolha == 2:
        salario = float(input('Informe o salário do funcionário: R$ '))
        ferias = salario + ((1/3) * salario)
        print(f'\n O salário do funcionário com o acréscimo das ferias é de R$ {ferias} reais.')
    if escolha == 3:
        salario = float(input('Informe o salário do funcionário: R$ '))
        meses_trabalhados = int(input('Agora, informe quantos meses ele trabalhou (MAX 12): '))
        salario13 = (salario * meses_trabalhados) / 12
        print(f'\n O décimo terceiro do funcionário será de R$ {salario13} reais, totalizando um salário de R$ {salario13 + salario} reais.')
    if escolha == 4:
        print('\n Sair do Programa! Obrigado por utilizar nosso serviço!')
        break
    else:
        print('Opção Inválida!')