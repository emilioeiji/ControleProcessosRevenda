#!/usr/binpython3
# -*- encoding: utf-8 -*-

""" 
	Verifica se o arquivo do web preços
	foi enviado ou não e retorna o status
	da consulta, 0 = não enviado, 1 = enviado
	Por: Emilio Eiji
	email: contato@emilioeiji.com.br
"""

import os
import sys
from datetime import datetime

# Definindo as variáveis necessárias
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


def pesquisa_saida():
    nome_arquivo_saida = []
    for arquivo_saida in dir_saida:
        lista_saida = arquivo_saida[0:12]
        nome_arquivo_saida.append(str(lista_saida))
    return (nome_arquivo_saida.count(wpsv))


def pesquisa_old():
    norme_arquivo_old = []
    for arquivo_old in dir_old:
        lista_old = arquivo_old[0:12]
        norme_arquivo_old.append(str(lista_old))
    return (norme_arquivo_old.count(wpsv))


def pesquisa_webprecos(diretorio):
    pass


resultado_saida = pesquisa_saida()
print("O resultado do diretório saida é: ", resultado_saida)

resultado_old = pesquisa_old()
print("O resultado do diretório old é: ", resultado_old)
