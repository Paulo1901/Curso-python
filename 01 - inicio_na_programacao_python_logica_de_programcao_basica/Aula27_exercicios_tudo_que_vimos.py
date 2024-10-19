"""
Exercícios
peça pro usuário digitar seu nome
peça pro usuário digitar sua idade
se nome e idade forem digitados
    Exiba:
        Seu noome é {nome}
        Seu nome invertido é {nome invertido}
        se nome contém (ou não) espaços
        seu nome tem {n} letras
        A primeira do seu nome é {letra}
        A utilma letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."

"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}') # exibido meu nome na tela
    print(f'Seu nome invertido {nome[::-1]}') #invertendi nome

if ' ' in nome: #condição se o nome tem espaço
    print('Seu nome contem espaços')
else:
    print('Seu nome não contem espaços')

    print(f'Seu nome tem {len(nome)} letras')# contando as letras do nome
    print(f'A primerira letra do seu nome é {nome[0]}') # primeira letra do nome
    print(f'A ultima letra do seu nome {nome[-1]}') # utima letra do nome

