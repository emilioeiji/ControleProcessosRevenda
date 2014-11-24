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
SQL = "SELECT cod_empregado, dat_inc, cod_usu_inc FROM log_relatorio WHERE cod_meta = 12 AND dat_inc between '2014-11-24 00:00:00.000' and '2014-11-24 23:59:00.000' ORDER BY cod_empregado"

cur = connection.cursor()
cur.execute(SQL)

rows = cur.fetchall()

codl = {}
datal = {}
usrl = {}
# Pode ser usado if row['id'] == id
for row in rows:
    cod = row[0]
    codl[cod] = cod
    dataInc = row[1]
    datal[cod] = dataInc
    usr = row[2]
    usrl[cod] = usr

cur.close()
connection.close()

dataEmissao = {}
for data in datal:
    dataEmissao[data] = datal[data].date()

horaEmissao = {}
for hora in datal:
    horaEmissao[hora] = datal[hora].time()

listaFuncionarios = []
arquivoFuncionario = open("listaFuncionarios.txt")
for linhaFuncionario in arquivoFuncionario:
    listaFuncionarios.append(int(linhaFuncionario))
arquivoFuncionario.close()

emitido = []
naoEmitido = []
validaStatus = {}
for verifica in listaFuncionarios:
    valida = verifica in codl
'''   
 	if valida == True:
        if horaEmissao < horaLimite:
        	print("Emitido antes do horario")
        validaStatus[verifica] = "Emitido"
    else:
        verifical.append(verifica)
        validaStatus[verifica] = "Não Emitido" 


if verifical == []:
    print("Relatórios emitidos para todos os setores.")
    sys.exit(0)
else:
    print("Não foram impressos os relatórios para os seguintes setores: ")
    for emiteStatus in validaStatus:
        print(emiteStatus)
    sys.exit(3)
'''