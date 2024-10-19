# Operador lógico 'not'
# Usado para inverter as expressções
# not True = False
# not false = true

# senha = input('Senha: ')

# if not senha:
# print('Você não digitou nada')
print(not False) # True
print(not True) # False

senha = input('Digite sua senha: ')

# Ánalisando primeiro a senha incorreta
# if senha != '1234':
#     print('senha incorreta')

if not senha:
    print('Você não digitou nada. ')

