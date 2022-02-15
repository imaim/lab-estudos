import os

FILE_NAME = 'variaveis_de_ambiente.py'

# Para Unix retorna a ultma modificação, para outros a data de criação
print(os.path.getctime(FILE_NAME))
# Retorna a ultima modificação
print(os.path.getmtime(FILE_NAME))
# Retorna o ultimo acesso
print(os.path.getatime(FILE_NAME))
# Verifica se é um arquivo
print(os.path.isfile(FILE_NAME))
# Verifica se é um diretorio
print(os.path.isdir(FILE_NAME))
# Verifica se é um link_simbolico
print(os.path.islink(FILE_NAME))
# Verifica se é um ponto simbolico
print(os.path.ismount(FILE_NAME))