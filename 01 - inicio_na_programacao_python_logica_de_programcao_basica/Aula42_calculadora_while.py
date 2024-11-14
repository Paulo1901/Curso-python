"""Calculadora"""

while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    #Checando os numero são validos
    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos.')
        continue

    #Checando se os operador são permitidos
    operador_permitidos = '+-/*'

    
    if operador not in operador_permitidos:
        print('Operador invalido.')
        continue

    if len(operador) > 1: #Testando a quatidade dos operadores
        print('Digite apenas 1 operador')

    print('Realizando a conta, confira o resultado a baixo: ')
    if operador == '+':
        print(f'{num_1_float}+{num_1_float}=',num_1_float + num_1_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_1_float}=',num_1_float - num_1_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_1_float}=',num_1_float / num_1_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_1_float}=',num_1_float * num_1_float)
    else:
        print('Nunca deveria chegar aqui ')

    sair = input('Quer sair? [s]im: ').lower().startswith('S')

    if sair is True:
        break



