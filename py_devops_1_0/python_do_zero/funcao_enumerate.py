## Copiado do arquivo for.py

cardapio = ['Carne','Queijo','Frango','Calabresa','Pizza','Carne Seca']

'''
print(cardapio[0])
print(cardapio[1])
print(cardapio[2])
'''

print('Pastelraria Devops')
print('Veja nosso Cardapio')
print('-------------------')
for indice,recheio in enumerate(cardapio):
    print(f'[{indice}]: {recheio}')


opcao = int(input('Digite o numero correspondete ao sabor desejado: '))
if opcao >= 0 and opcao <= len(cardapio):
    print(f'O sabor escolhido foi {cardapio[opcao]}')
else:
    print(f'Opção invalida')