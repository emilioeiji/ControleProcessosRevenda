#!/usr/binpython3
# -*- encoding: utf-8 -*-

""" Verifica se o arquivo do web preços
	foi enviado ou não e retorna o status
	da consulta
"""


from datetime import datetime


now = datetime.now()
datahora = ("%s/%s/%s %s:%s:%s" %
            (now.day, now.month, now.year, now.hour, now.minute, now.second))
