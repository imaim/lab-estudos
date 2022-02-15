#!/bin/bash

BASE=master
SSH_USR="root"
SSH_PWD="2Cm@ll098#"
IP_BKP_NUVEM="172.16.10.9"
SSH_OPT="-o GSSAPIAuthentication=no -o  StrictHostKeyChecking=no"
#SSH_OPT=

# SRVBKP > Servidor de Backup nuvem
# Servidor 1 > 2226
# Servidor 2 > 2227
SRVBKP=2226

# TBKP > tipo de backup
# 1 > Multibase
# 2 > Base Unica  2coml
TBKP=1

if [ ${TBKP} -eq 1 ]
    then 
        #echo "mutibase"
        BACKUPS=$(sshpass -p "${SSH_PWD}" ssh ${SSH_OPT} -p ${SRVBKP} ${IP_BKP_NUVEM} \
        -l ${SSH_USR} "ls -rt /gluster/volume2/cloud/${SSH_USR} |grep \"backup\" | grep ${BASE}; find /gluster/volume2/cloud/${SSH_USR} -name \"b*${BASE}*.z\" -mtime -3 | wc -l")

        QUANTIDADE_BACKUP=$(echo "${BACKUPS}"|grep ${BASE} | wc -l)

        LISTARS=$(echo "${BACKUPS}"|grep ${BASE} |tail -n 10)
        LISTAR=$(echo ${LISTARS} | xargs -d"\n")

        BACKUP=$(echo "${BACKUPS}"| egrep '^(0{0,2}[0-9]|0?[1-9][0-9]|[1-9][0-9][0-9])$' | tail -1)

else
        #echo "base simples"
        BACKUPS=$(sshpass -p "${SSH_PWD}" ssh ${SSH_OPT} -p ${SRVBKP} ${IP_BKP_NUVEM} \
        -l ${SSH_USR} "ls -rt /gluster/volume2/cloud/${SSH_USR} |grep \"backup\"; find /gluster/volume2/cloud/${SSH_USR} -name \"b*.z\" -mtime -3 | wc -l")

        QUANTIDADE_BACKUP=$(echo "${BACKUPS}"|grep backup| wc -l)

        LISTARS=$(echo "${BACKUPS}"|grep backup |tail -n 10)
        LISTAR=$(echo ${LISTARS} | xargs -d"\n")

        BACKUP=$(echo "${BACKUPS}"| egrep '^(0{0,2}[0-9]|0?[1-9][0-9]|[1-9][0-9][0-9])$' | tail -1)

fi

if [ -n "${BACKUP}" ];
        then
                if [ ${BACKUP} -ge 2 ]
                then
                    echo "0 List_Backup_Nuvem_"${BASE}" result=0;1;2;0;2 OK - Encontrados = ${QUANTIDADE_BACKUP} --- ARQUIVOS  ${LISTAR}  "
                    exit 0

                elif [  ${BACKUP} -ge 1 ]
                then
                    echo "1 List_Backup_Nuvem_"${BASE}" result=1;1;2;0;2 WARN - Qde Backup Insuficiente =${QUANTIDADE_BACKUP} --- ARQUIVOS  ${LISTAR} "
                    exit 1

                elif [ ${BACKUP} -lt 1 ]
                then
                    echo "2 List_Backup_Nuvem_"${BASE}" result=2;1;2;0;2 CRITICAL - Nenhum Backup Encontrado."
                    exit 2

                else
                    echo "3 List_Backup_Nuvem_"${BASE}" result=3;1;2;0;2 UNKNOWN - Erro ao tentar Encontrar backup"
                    exit 3
        fi
else 
    echo "3 List_Backup_Nuvem_"${BASE}" result=3;1;2;0;2 UNKNOWN - Erro ao tentar Encontrar backup"
    exit 3
fi
exit


