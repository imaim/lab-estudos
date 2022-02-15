import re

with open("nomes.txt") as file:
    lines = file.read()
    parametros = r'[\w]+ Silva'
    # todas as recorrencias
    regex = re.findall(parametros, lines)
    print(f'Os nomes são :{regex}')
    regex = re.search(parametros, lines)
    print(f'Os nomes são :{regex.group()}')
    regex = re.match(parametros, lines)
    print(f'Os nomes são :{regex.group()}')
