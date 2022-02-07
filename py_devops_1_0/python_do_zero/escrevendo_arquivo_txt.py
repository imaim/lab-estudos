clientes = ['Gustavo', 'Carlos', 'Lucas', 'Pedro', 'Paulo', 'Jackson', 'Jose']
file = open('cliente.txt', 'w')
for cliente in clientes:
    print(f'Cliente {cliente} adicionado na lista')
    file.write(f'{cliente}\n')
file.close