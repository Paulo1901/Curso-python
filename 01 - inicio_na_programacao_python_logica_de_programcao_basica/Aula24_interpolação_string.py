"""
Interpolação básica de strings
5 - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF123456789)

"""

nome = 'Paulo'
preco = 1000.987799887
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)
print('O hexadecimal de %d é %05x ' % (349, 349))