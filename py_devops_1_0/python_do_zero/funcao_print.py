
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
print(nome_estabelecimento, end='\n=========================\n\n') #testando caracter de separação
print(pastel1, valor_pastel1, status, sep='==>', end='\n\n') #testando caracter de separação
print(pastel2, valor_pastel2, status, sep=';') # simulando saida com ponto e virgula utilizado por csv
print(pastel3, valor_pastel3, status, sep='\n', end='\n\n')  #validando sainda
print(pastel4, valor_pastel4, status, sep='\n', end='\n\n') #validando sainda
