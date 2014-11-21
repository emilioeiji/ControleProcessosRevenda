#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import pypyodbc
#connection_string = ('Driver={SQL Server Native Client 11.0};Server=<172.16.56.241>;Database=<OPVD>;Uid=<sa>;Pwd=<sa>;')
connection_string = ('Driver=FreeTDS;Server=172.16.56.241;port=1433;uid=sa;pwd=sa;database=opvd')
connection = pypyodbc.connect(connection_string)
SQL = "SELECT cod_empregado, dat_inc, cod_usu_inc FROM log_relatorio WHERE cod_meta = 12 AND dat_inc between '2014-11-06 00:00:00.000' and '2014-11-06 23:59:00.000' ORDER BY cod_empregado"

cur = connection.cursor()
cur.execute(SQL)

rows = cur.fetchall()

for row in rows:
	print(row)

cur.close()
connection.close()
