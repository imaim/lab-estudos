#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# yapf: disable
# type: ignore
r'''
Teste de execucao
'''
import os 
import glob
from pathlib import Path
from pathlib import PureWindowsPath


#caminho = str(PureWindowsPath('c:/backup_auto/lab-estudos/pratica/'))
#caminho =  PureWindowsPath('c:/backup_auto/lab-estudos/pratica/')
diretorio = 'c:/backup_auto/lab-estudos/pratica/'
for arquivo in os.listdir(f'{diretorio}') :
    data = os.path.getmtime(diretorio + arquivo)
    print(f'a data de modificação do arquivo {arquivo} é {data}')
    

