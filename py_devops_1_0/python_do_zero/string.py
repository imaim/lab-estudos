
nome_estabelecimento = 'Pastelaria Devops'
pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Calabresa'
pastel5 = "Carne com queijo"
pastel6 = " Carne com frango "

print('--------------------')
print('')

print('substituindo caracteres')
novo_sabor = pastel5.replace('queijo','frango')
print(novo_sabor)
print(pastel5.upper())
print(pastel5.lower())
print(pastel5.startswith('Queijo'))
print(pastel5.startswith('Carne'))
print(pastel5.endswith('frango'))
print(pastel5.endswith('queijo'))
print('Pastel 6:', pastel6)
print('Pastel 6:', pastel6.replace(' ','-'))
novo_pastel6 = pastel6.strip()
novo_pastel6 = novo_pastel6.replace(' ','-')
print('Pastel 6:', novo_pastel6)
novo_pastel6 = pastel6.lstrip()
novo_pastel6 = novo_pastel6.replace(' ','-')
print('Pastel 6:', novo_pastel6)
novo_pastel6 = pastel6.rstrip()
novo_pastel6 = novo_pastel6.replace(' ','-')
print('Pastel 6:', novo_pastel6)

print('### Função LEN ###')
print('Quantidade de caracteres no pastel 5:', len(pastel5))

print('### Fatiamento ###')
print(pastel5)
# 0 1 2 3 4 
# c a r n e
# -4 -3 -2 -1
print(pastel5[0])
print(pastel5[-1])
print(pastel5[0:2])
print(pastel5[0:5])
print(pastel5[2:])
print(pastel5[:4])

print('Operadores IN e NOT IN')
result = 'Frango' in pastel5
print(result)
result = 'Frango' not in pastel5
print(result)