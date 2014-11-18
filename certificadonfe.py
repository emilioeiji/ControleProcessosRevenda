#/usr/bin/python3
# -*- encoding: utf-8 -*-

from datetime import datetime


vencimento = datetime(2015, 6, 16)
hoje = datetime.now()
dias_vencimento = vencimento - hoje

print(dias_vencimento.days)
