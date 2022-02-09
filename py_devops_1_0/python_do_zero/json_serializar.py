import json

meus_pedidos = {
    'estabelecimento': 'Pastelaria DevOps',
    'pedidos': [
        {
            'cliente': 'Carlos',
            'valor': 24.00
        },
        {
            'cliente': 'Jose',
            'valor': 34.00
        }
    ],
}
print(meus_pedidos)
print(type(meus_pedidos))

json_data = json.dumps(meus_pedidos, indent=4)
print(type(json_data))
print(json_data)

## with --- metodo de tratativa de arquivo (não precisa afechar, so funciona dentro do bloco do with )
with open('meus_pedidos.json', 'w') as file:
    json.dump(meus_pedidos, file, indent=4)

print('Serialização Finalizada')