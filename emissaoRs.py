#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import pypyodbc
import os
import sys
from datetime import datetime


agora = datetime.now()
horaLimite = agora.replace(hour=9, minute=0, second=0, microsecond=0)

connection_string = ('Driver=FreeTDS;Server=172.16.56.241;port=1433;uid=sa;pwd=sa;database=opvd')
connection = pypyodbc.connect(connection_string)
SQL = "SELECT cod_empregado, dat_inc, cod_usu_inc FROM log_relatorio WHERE cod_meta = 12 AND dat_inc between '2014-11-21 00:00:00.000' and '2014-11-21 23:59:00.000' ORDER BY cod_empregado"

cur = connection.cursor()
cur.execute(SQL)

rows = cur.fetchall()

datal = {}
usrl = {}
# Pode ser usado if row['id'] == id
for row in rows:
    cod = row[0]
    data = row[1]
    datal[cod] = data
    usr = row[2]
    usrl[cod] = usr

cur.close()
connection.close()

datav = datal[99998]
hora = datal[99998]

if hora.time() < horaLimite.time():
    print('Abaixo da hora limite')
else:
    print('Acima da hora limite')

listaFuncionarios = []
arquivoFuncionario = open("listaFuncionarios.txt")
for linhaFuncionario in arquivoFuncionario:
	listaFuncionarios.append(int(linhaFuncionario))
arquivoFuncionario.close()

print(listaFuncionarios)