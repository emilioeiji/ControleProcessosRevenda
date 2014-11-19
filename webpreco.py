#!/usr/bin/python3
# -*- encoding: utf-8 -*-

""" 
	Verifica se o arquivo do web preços
	foi enviado ou não e retorna o status da pesquisa
	0 = ok, 1 = warning, 2 = critical, 3 = uknown
	Por: Emilio Eiji
	email: contato@emilioeiji.com.br
"""

import os
import sys
from datetime import datetime

# Definindo as variáveis necessárias
# Utilizar weekday() para verificar o domingo
now = datetime.now()
datahora = ("%s/%s/%s %s:%s:%s" %
            (now.day, now.month, now.year, now.hour, now.minute, now.second))
wpsv = ("WPSV%s%s%s" % (now.year, now.month, now.day))
# Definir o diretório de pesquisa onde ficam os arquivos a serem enviados.
saida = '/media/promax/int/sftp/saida/'
dir_saida = os.listdir(saida)
# Definir o diretório de pesquisa onde ficam os arquivos já enviados.
old = '/media/promax/int/sftp/old/'
dir_old = os.listdir(old)


def pesquisa_arquivo(diretorio):
    nome_arquivo = []
    for arquivo in diretorio:
        lista_arquivo = arquivo[0:12]
        nome_arquivo.append(str(lista_arquivo))
    return (int(nome_arquivo.count(wpsv)))


def pesquisa_webprecos():
    if pesquisa_arquivo(dir_saida) == 1 and pesquisa_arquivo(dir_old) == 1:
        print("UKNOWN - Arquivo %s em transiçao." % wpsv)
        sys.exit(3)
    elif pesquisa_arquivo(dir_saida) == 1:
        print("WARNING - Arquivo parado no diretório saida.")
        sys.exit(1)
    elif pesquisa_arquivo(dir_old) == 1:
        print("OK - Arquivo %s enviado com sucesso." % wpsv)
        sys.exit(0)
    else:
        print("CRITIAL - Arquivo %s não encontrado." % wpsv)
        sys.exit(2)


pesquisa_webprecos()
