# operador lógico 
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# todas a expressão como verdadeira.
# se qualquer valor for considerado verdadeiro]
# toda expressão inteira será avaliada naquele valor.
# São considerados falsy (que você ja viu)
# 0, 0.0 '' false
# também existe o tipo none que é
# usado para representar um não valor

#VARIAVEIS
# entrada = input('[E]entrar [S]sair')
# senha_digitada = input('Senha: ')
# senha_permitida = '1234'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

#Avaliação de curto circuito
# print(True or False)
senha = input('Senha: ') or 'sem senha'
print(senha)


