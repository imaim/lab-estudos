import csv


create_file = open('pedidos.csv', 'w', newline='', encoding='utf-8')
escritor = csv.writer(create_file, delimiter=';')
leitor = ['ID', 'Cliente', 'Valor Total']
escritor.writerow(leitor)

pedido1 = ['01', 'Jose', '24.00']
escritor.writerow(pedido1)
pedido2 = ['02', 'Carlos', '30.00']
escritor.writerow(pedido2)
pedido3 = ['03', 'Lucas', '47.00']
escritor.writerow(pedido3)

create_file.close()