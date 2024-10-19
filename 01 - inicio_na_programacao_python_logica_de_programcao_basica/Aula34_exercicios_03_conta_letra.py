"""
3)Faça um programa que peça o peimwiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva (seu nome é curto; se tiver entre 5 e 6 letras, escreva 
Seu nome é nomal; maior que 6 escreva seu nome é muito grande)

"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite pelo menos uma letra')