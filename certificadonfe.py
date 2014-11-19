#!/usr/bin/python3
# -*- encoding: utf-8 -*-

""" 
	Verifica a validade do certificado digital
	e retorna se o período é maios que 30 dias até o vencimento.
	0 = ok, 1 = warning, 2 = critical, 3 = uknown
	Por: Emilio Eiji
	email: contato@emilioeiji.com.br
"""

import os
import sys
from datetime import datetime


dataVencimento = datetime(2015, 6, 16)


def verificaVencimento(vencimento):
    hoje = datetime.now()
    diasVencimento = vencimento - hoje
    if diasVencimento.days > 30:
        print("OK - Certificado vence em: %s dias" % diasVencimento.days)
        sys.exit(0)
    elif diasVencimento.days > 15:
        print("WARNING - O certificado vence em: %s dias" % diasVencimento.days)
        sys.exit(1)
    elif diasVencimento.days > 7:
        print("CRITICAL - Faltam apenas %s para renovar o certificado" %
              diasVencimento.days)
        sys.exit(2)
    elif diasVencimento.days > 3:
        print("CRITICAL - A casa caiu, corre que falta só %s dias" %
              diasVencimento.days)
        sys.exit(2)
    else:
        print("UKNOWN - Erro inesperado!")
        sys.exit(3)

verificaVencimento(dataVencimento)
