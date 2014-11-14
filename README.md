Controles Processos Revenda
======

Escopo
=====

Verifica Web Preços

	Acessar diretório Promax\int\sftp\saida
	Verificar se existe o arquivo WPSVAAAAMMDD*.crp
		Se existir o arquivo o envio do mesmo está pendente
		Registrar como não enviado
	Acessar diretório Promax\int\sftp\old
	Verificar se existe o arquivo WPSVAAAAMMDD*.crp
		Se existir o arquivo o envio do mesmo está ok
		Registrar como enviado.
	O script irá retornar os seguintes valores:
	0 = Para enviado - OK
	1 = Para não enviado - Warning
	2 = Para arquivo não encontrado - Critial
	3 = Para arquivo em transição - Uknown
