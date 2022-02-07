## nao aceita valor repetido

pedidos_dia1 = [
    {'Cliente': 'Jose', 'pastel': 'Queijo'},
    {'Cliente': 'Jose', 'pastel': 'Queijo'},
    {'Cliente': 'Pedro', 'pastel': 'Carne'},
    {'Cliente': 'Lucas', 'pastel': 'Queijo'},
    {'Cliente': 'Carlos', 'pastel': 'Frango'},
]

pedidos_dia2 = [
    {'Cliente': 'Marcos', 'pastel': 'Pizza'},
    {'Cliente': 'Daniel', 'pastel': 'Queijo'},
    {'Cliente': 'Pedro', 'pastel': 'Carne'},
    {'Cliente': 'Lucas', 'pastel': 'Queijo'},
    {'Cliente': 'Carlos', 'pastel': 'Frango'},
]

cliente_dia1 = set()
for pedido in pedidos_dia1:
    cliente_dia1.add(pedido['Cliente'])

print(f'Dia 1: {cliente_dia1}')

cliente_dia2 = set()
for pedido in pedidos_dia2:
    cliente_dia2.add(pedido['Cliente'])

print(f'Dia 2: {cliente_dia2}')

todos_cliente = cliente_dia1 | cliente_dia2
print(f'União: {todos_cliente}')

clientes_comprou_todos_os_dias = cliente_dia1.intersection(cliente_dia2)
print(f'Interseção: {clientes_comprou_todos_os_dias}')

clientes_diferenca = cliente_dia1 - cliente_dia2
print(f'Diferenca: {clientes_diferenca}')