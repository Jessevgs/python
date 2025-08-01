
print('***calculadora***')

while True:
    
    num1 = input('Primeiro numero: ')
    num2 = input('Segundo numero: ')

    print('Escolha a operacao:')
    print('1 - Adicao')
    print('2 - Subtracao')
    print('3 - Multiplicacao')
    print('4 - Divisao')

    operacao = input('Operacao: ')

    if operacao == '1':
        resultado = float(num1) + float(num2)
        print(f'Resultado: {resultado}')
    elif operacao == '2':
        resultado = float(num1) - float(num2)
        print(f'Resultado: {resultado}')
    elif operacao == '3':
        resultado = float(num1) * float(num2)
        print(f'Resultado: {resultado}')
    elif operacao == '4':
        if float(num2) != 0:
            resultado = float(num1) / float(num2)
            print(f'Resultado: {resultado}')
        else:
            print('Erro: Divisao por zero!')
    else:
        print('Operacao invalida!')
    
    sair = input('Deseja sair? [s]im [n]ao: ').lower().startswith('s')

    if sair is True:
        break
              
    print(sair)