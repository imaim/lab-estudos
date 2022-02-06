'''
pastel1 = 'carne'
pastel2 = 'queijo'
pastel3 = 'frango'
pastel4 = 'Calabresa'
'''

cardapio = ['Carne','Queijo','Frango','Calabresa']
print(cardapio)

print(f'Tamanho da Lista {len(cardapio)} itens')
print(f'Acessando o primeiro item da lista: {cardapio[0]}')
print(f'Acessando o segundo item da lista: {cardapio[2]}')

print(f'Acessando o ultimo item da lista: {cardapio[-1]}')
print(f'Acessando o penultimo item da lista: {cardapio[-2]}')

# Queijo = Mussarela
cardapio[1] = 'Mussarela'
print(cardapio)

print('-------')

novo_cardapio = []
print(len(novo_cardapio))
print(type(novo_cardapio))

print('')
print('Adicionando elementos na lista')
novo_cardapio.append('Carne')
novo_cardapio.append('Queijo')
novo_cardapio.append('Frango')
novo_cardapio.append('Calabresa')
print(novo_cardapio)

print('-------')
print('')
print('Acessando trexos da lista')

print(novo_cardapio[1:3])
print(novo_cardapio[2:])
print(novo_cardapio[:3])

print('-------')
print('')
print('Organizando em ordem alfabetica')
print(novo_cardapio)
print(sorted(novo_cardapio, key=str.lower))

print('')
novo_cardapio.remove('Calabresa')
print(novo_cardapio)

print('')
novo_cardapio.append('Frango')
novo_cardapio.append('Frango')
print(novo_cardapio.count('Frango'))

novo_cardapio.insert(0,'Palmito')
novo_cardapio.insert(2,'Pizza')
print(novo_cardapio)

print(novo_cardapio.pop(4))
print(novo_cardapio)

print(novo_cardapio.pop())

del novo_cardapio[3:]
print(novo_cardapio)


print('-------')
print('')

vendas = []
vendas.append(24.00)
vendas.append(16.00)
vendas.append(24.00)
print(vendas)
print(sum(vendas))
print(max(vendas))
print(min(vendas))
print(f'{sum(vendas)/len(vendas):.2f}')


numeros = list(range(1,101))
print(numeros)
print(len(numeros))
del numeros[:10]
print(numeros)
del numeros[:10]
del numeros[:10]
print(numeros)
print(numeros[:10])