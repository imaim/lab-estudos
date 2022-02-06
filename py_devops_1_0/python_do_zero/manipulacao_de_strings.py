
nome_estabelecimento = "Pastelaria Devops"
pastel1 = "Carne"
pastel2 = "Queijo"
pastel3 = "Frango"
pastel4 = "Calabresa"
status = True
valor_pastel1 = 6.0
valor_pastel2 = 6.0
valor_pastel3 = 6
valor_pastel4 = 6

# print(nome_estabelecimento)
'''
print(pastel1, valor_pastel1, status)
print(pastel2, valor_pastel2, status)
print(pastel3, valor_pastel3, status)
print(pastel4, valor_pastel4, status)

'''

print('Concatenacao')
print('')
mensagem = 'O nome do stabelecimento é ' + nome_estabelecimento
print(mensagem)
mensagem2 = 'O pastel de ' + pastel1 + 'custa R$: ' + str(valor_pastel1)
print('')
print('Interpolacao')
print('')
print('O nome do stabelecimento é %s' %nome_estabelecimento)
print('O pastel de %s custa R$ %f' %(pastel1,valor_pastel1))
print('O pastel de %s custa R$ %.2f' %(pastel1,valor_pastel1))
print('O pastel de %s custa R$ %.3f' %(pastel1,valor_pastel1))
print('O pastel de %s custa R$ %d' %(pastel3,valor_pastel3))
print('O pastel de %s custa R$ %.3d' %(pastel1,valor_pastel1))

print('')
print('metodo Format')
print('')
print('O nome do stabelecimento é {}' .format(nome_estabelecimento))
print('O pastel de {} custa R$ {}' .format(pastel1,valor_pastel1))
print('O pastel de {} custa R$ {:.2f}' .format(pastel1,valor_pastel1))
print('O pastel de {} custa R$ {:.3f}' .format(pastel1,valor_pastel1))
print('O pastel de {} custa R$ {}' .format(pastel3,valor_pastel3))
print('O pastel de {} custa R$ {:05}' .format(pastel1,valor_pastel1))

print('')
print('metodo F-String')
print('')
print(f'O nome do stabelecimento é {nome_estabelecimento}')
print(f'O pastel de {pastel1} custa R$ {valor_pastel1}')
print(f'O pastel de {pastel1} custa R$ {valor_pastel1:.2f}')
print(f'O pastel de {pastel1} custa R$ {valor_pastel1:.3f}')
print(f'O pastel de {pastel3} custa R$ {valor_pastel3}')
print(f'O pastel de {pastel1} custa R$ {valor_pastel1:.5f}')
