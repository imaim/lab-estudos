cardapio = {}
print(type(cardapio))

pastel1 = {'sabor': 'queijo', 'valor': 6.00, 'status': True}
print(pastel1['sabor'])
print(pastel1['valor'])
print(pastel1['status'])
#print(pastel1['quantidade']) # key error, chave n encontrada

pastel1['valor'] = 7.00
print(pastel1)

print(pastel1.get('quantidade'))
print(pastel1.get('status'))
if pastel1.get('quantidade'):
    print(pastel1.get('quantidade'))
else:
    pastel1['quantidade'] = 10

print(pastel1)

keys = pastel1.keys()
print(keys)

for key in keys:
    if key == 'status':
        print(f'{key} foi encontrado')
    else:
        pass

values = pastel1.values()
print(values)
for value in values:
    print(f'O elemento {value} está no dicionario')

dict_values = pastel1.items()
for key, value in dict_values:
    print(f' a chave {key} possui o valor {value}')

pastel1.pop('quantidade')
print(pastel1)

pastel1.pop('status')
print(pastel1)