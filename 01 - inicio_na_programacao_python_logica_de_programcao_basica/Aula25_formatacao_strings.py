"""
Formatação básica de strings
s - string
d - int
f - float
(numero de digitos)f
x ou X - Hexadecimal
> - esquerda
< - direita
^ - centro
sinal - + ou -
Ex: 0>-100,.1f
conversion flags - !r !s !a

"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1223.009883883:0=+10,.1f}')

