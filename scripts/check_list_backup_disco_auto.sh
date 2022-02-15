#!/bin/bash

BASE=WINT
DIR_BACKUP_LOCAL="/db/backup/backup_old"

QUANTIDADE_BACKUP=$(ls ${DIR_BACKUP_LOCAL} | grep "$BASE_" | wc -l)
LISTAR=$(ls -tr ${DIR_BACKUP_LOCAL} | grep "$BASE" | tail -n 10 | xargs -d'\n')
BACKUP=$(find ${DIR_BACKUP_LOCAL} -maxdepth 1 -name "b*$BASE*.z" -mtime -3 | wc -l)

        if [ $BACKUP -ge 2 ]
        then
        echo "0 List_Backup_Disco_${BASE} result=0;1;2;0;2 OK - Encontrados = $QUANTIDADE_BACKUP --- ARQUIVOS  $LISTAR  "
        exit 0

        elif [  $BACKUP -eq 1 ]
        then
        echo "1 List_Backup_Disco_${BASE} result=1;1;2;0;2 WARN - Qde Backup Insuficiente =$QUANTIDADE_BACKUP--- ARQUIVOS  $LISTAR "
        exit 1


        elif [ $BACKUP -lt 1 ]
        then
        echo "2 List_Backup_Disco_${BASE} result=2;1;2;0;2 CRITICAL -- ARQUIVOS  $LISTAR"
        exit 2

        else
        echo "3 List_Backup_Disco_${BASE} result=3;1;2;0;2 UNKNOWN - Erro ao tentar Encontrar backup"
        exit 3
        fi