#!/usr/binpython3
# -*- encoding: utf-8 -*-

""" 
	Verifica se o arquivo do web preços
	foi enviado ou não e retorna o status
	da consulta
	Por: Emilio Eiji
	email: contato@emilioeiji.com.br
"""

import os
import sys
from datetime import datetime


now = datetime.now()
datahora = ("%s/%s/%s %s:%s:%s" %
            (now.day, now.month, now.year, now.hour, now.minute, now.second))
wpsv = ("WPSV%s%s%s" % (now.year, now.month, now.day))


def pesquisa_webprecos(diretorio):
    #lista = []
    nome_arquivo = []
    for arquivo in diretorio:
        lista = arquivo[0:12]
        nome_arquivo.append(str(lista))
    return (nome_arquivo.count(wpsv))


saida = '/media/promax/int/sftp/saida/'
dir_saida = os.listdir(saida)
old = '/media/promax/int/sftp/old/'
dir_old = os.listdir(old)

resultado = pesquisa_webprecos(dir_old)
print(resultado)
