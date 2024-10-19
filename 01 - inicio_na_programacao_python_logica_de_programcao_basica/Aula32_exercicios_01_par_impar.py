"""
1)Faça um programa que peça ao usuário digigitar um número inteiro,
informe se este número é par ou impar. caso o usuário não digite um número
inteiro, informe que não é um número inteiro

"""
# UMA DAS SOLUÇÕES

entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'Par'
    
#     print(f'O número  {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro. ')

# OUTRA FORMA DE RESOLUÇÃO

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'Par'
    
    print(f'O número  {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro. ')