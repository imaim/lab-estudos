#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os

caminho = "/db/backup/backup_old"
lista_arquivos = os.listdir(caminho)
lista_datas = []
for arquivo in lista_arquivos:
    # descobrir a data desse arquivo
    if ".tar.z" in arquivo:
        data = os.path.getmtime(caminho + arquivo)
        lista_datas.append((data, arquivo))
    
    # data inicial = 01/01/2021
    # data1 = 02/01/2021 -> 10.000
    # data2 = 15/02/2021 -> 150.000
    
lista_datas.sort(reverse=True)
ultimo_arquivo = lista_datas[0]
print(ultimo_arquivo[1])

