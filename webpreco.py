#!/usr/binpython3
# -*- encoding: utf-8 -*-

""" 
	Verifica se o arquivo do web preços
	foi enviado ou não e retorna o status da pesquisa
	0 = não enviado, 1 = enviado, -1 = transição, -2 = arquivo nao encontrado
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
    return (int(nome_arquivo_saida.count(wpsv)))


def pesquisa_old():
    norme_arquivo_old = []
    for arquivo_old in dir_old:
        lista_old = arquivo_old[0:12]
        norme_arquivo_old.append(str(lista_old))
    return (int(norme_arquivo_old.count(wpsv)))


def pesquisa_webprecos():
    if pesquisa_saida() == 1 and pesquisa_old() == 1:
        return (int(-1))
    elif pesquisa_saida() == 1:
        return (int(0))
    elif pesquisa_old() == 1:
        return (int(1))
    else:
        return (int(-2))


""" Validação
resultado_saida = pesquisa_saida()
print("O resultado do diretório saida é: ", resultado_saida)

resultado_old = pesquisa_old()
print("O resultado do diretório old é: ", resultado_old)
"""
resultado = pesquisa_webprecos()
print("O resultado da presquisa web preços é: ", resultado)

if pesquisa_webprecos() == 0:
	print("Arquivo %s parado no diretório saida." % (wpsv))
elif pesquisa_webprecos() == 1:
	print("Arquivo %s enviado." % (wpsv))
elif pesquisa_webprecos() == -1:
	print("Arquivo %s em transição." % (wpsv))
elif pesquisa_webprecos() == -2:
	print("O arquivo %s não foi encontrado." % (wpsv))
else:
	print("Erro desconhecido.")