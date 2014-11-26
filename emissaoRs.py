#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import pypyodbc
import os
import sys
from datetime import datetime


agora = datetime.now()
horaInicio = agora.replace(hour=7, minute=0, second=0, microsecond=0)
horaInicio = horaInicio.time()
horaLimite = agora.replace(hour=9, minute=0, second=0, microsecond=0)
horaLimite = horaLimite.time()

try:
    connection_string = (
        'Driver=FreeTDS;Server=0.0.0.0;port=1433;uid=id;pwd=pw;database=db')
    connection = pypyodbc.connect(connection_string)
except:
    print("Ocorreu algum erro na conexão.")
    sys.exit()

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
verifical = []
validaStatus = {}

"""
def verificaStatus(saida, msg):
    for verifica in listaFuncionarios:
        valida = verifica in codl
        if valida == True:
            emitido.append(verifica)
            validaStatus[verifica] = "Ok"
        else:
            naoEmitido.append(verifica)
            verifical.append(verifica)
            validaStatus[verifica] = "NOk"
    if verifical == []:
        print(msg)
        sys.exit(saida)
    else:
        print("Oops - Não foram emitidos para os setores: ")
        sys.exit(saida)
"""

for verificaHora in listaFuncionarios:
    if horaEmissao[verificaHora] > horaInicio and horaEmissao[verificaHora] < horaLimite:
        #verificaStatus(0, "ok - Relatórios emitidos dentro do horário limite.")
        emitido.append(verificaHora)
        #print("OK - Setor: %s - Hora: %s" %
        #      (verificaHora, horaEmissao[verificaHora]))
    else:
        naoEmitido.append(verificaHora)
        verifical.append(verificaHora)
        #print("NOK - Setor: %s - Hora: %s" %
        #      (verificaHora, horaEmissao[verificaHora]))

if verifical == []:
	print("Todos os setores emitidos antes do horário limite.")
else:
	print(emitido)
	print(naoEmitido)
