'''
mensagem_boasvindas = 'Seja bem vindo a pastelaria devops'

nome_pedido1 = 'Carlos'
sabor_pedido1 = 'Frango'

nome_pedido2 = 'Pedro'
sabor_pedido2 = 'Queijo'

print(f'O {nome_pedido1} pediu pastel de {sabor_pedido1}')
print(f'O {nome_pedido2} pediu pastel de {sabor_pedido2}')
'''

def mensagem_boasvindas(nome):
    print(f'Seja Bem vindo a Pastelaria {nome}')

def add_pedidos(cliente,sabor):
    if len(cliente) < 1 :
        msg_err = 'Insira o nome do Cliente corretamente'
        return msg_err
    novo_pedido = f'O {cliente} pediu pastel de {sabor}'
    return novo_pedido

mensagem_boasvindas(nome='DevOps')
pedido1 = add_pedidos(cliente='Robert', sabor='Frango')
print(pedido1)
pedido2 = add_pedidos('Jose','Queijo')
print(pedido2)
pedido3 = add_pedidos('','Pizza')
print(pedido3)
