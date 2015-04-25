"""
Biblioteca criada com todas as funções criadas em Programação 2
"""

"""
Um n-grama é uma sequência de caracteres de tamanho n, por exemplo:
"goiaba" --> 1-grama: g, o, i, a, b, a
			 2-grama: go, oi, ia, ab, ba
			 3-grama: goi, oia, iab, aba
			 ...
Construa a função ngrama(<texto>, <tam>) que retorna uma  lista contendo os n-gramas de tamanho <tam> de <texto>
"""

def nGrama(pTexto, tam):
	ngramas = []
	
	for i in range(len(pTexto)):
		if i <= len(pTexto) - tam:
			ngramas.append(pTexto[i: tam + i])
		#
	#
	return ngramas
#

def insereEspacos(pTexto):
	strSeparadores = " .,:;!?(){}[]/\\"
	textoNovo = ""
	
	for elem in pTexto:
		if elem in strSeparadores:
			if elem != "":
				textoNovo += " " + elem + " "
			else:
				textoNovo += elem
			#
		else:
			textoNovo += elem
		#
	#
	return textoNovo
#

def tokenizador(txt):
	lstTokens = []
	strbuffer = ''
	lstposicoes = []
	pos = 0
	separador = ' ,!?.:;/-_\\()[]{}'
	
	for pos in range(len(txt)):
		if txt[pos] not in separador:
			strbuffer += txt[pos]
		else:
			if strbuffer != '':
				lstTokens.append(strbuffer)
				lstposicoes.append(pos-len(strbuffer))
				strbuffer = ''
			if txt[pos] not in [' ','\t']:
				lstTokens.append(txt[pos])
				lstposicoes.append(pos)
	if strbuffer != '':
		lstTokens.append(strbuffer)
		lstposicoes.append(pos-len(strbuffer))
	
	return lstTokens, lstposicoes
#
	
def separaPal(pTexto):
	strSeparadores = ' ,!?.:;/-_\\()[]{}'
	strBuffer = ""
	lstPalavras = []
	
	for i in range(len(pTexto)):
		if pTexto[i] not in strSeparadores:
			strBuffer += pTexto[i]
		elif strBuffer != "":
			lstPalavras.append(strBuffer)
			strBuffer = ""
		#
	#
	if strBuffer != "":
		lstPalavras.append(strBuffer)
	#
	return lstPalavras			
#

def separaPal2(pTexto):
	textoAux = insereEspacos(pTexto)
	lstPals = textoAux.split()
	pos = 0
	
	for pos in range(len(lstPals)):
		if not pos.isalpha():
			del(pos)
		else:
			pos += 1
		#
	#
	return lstPals
#

def intersec(pTexto1, pTexto2):
	lstTexto1 = separaPal(pTexto1)
	lstTexto2 = separaPal(pTexto2)
	inter = []
	
	for texto1 in lstTexto1:
		for texto2 in lstTexto2:
			if texto1 == texto2:
				if texto1 not in inter:
					inter.append(texto1)
				#
			#
		#
	#
	return inter
#

def corrente(pTexto, pPosicao):
	strSeparadores = " ,.:;!?"
	esquerda = pPosicao; direita = pPosicao; palavra = "Não tem nada aqui :/"
	
	if pTexto[esquerda] not in strSeparadores:
		while esquerda >= 0 and pTexto[esquerda] not in strSeparadores:
			esquerda -= 1
		#
		while direita < len(pTexto) and pTexto[direita] not in strSeparadores:
			direita += 1
		#
		palavra = pTexto[esquerda + 1:direita]
	else:
		palavra = "None"
	#
	return palavra
#

def anterior(pTexto, pPosicao):
	strSeparadores = " ,.:;!?"
	aux = pPosicao
	
	if pTexto[aux] not in strSeparadores:
		while aux >= 0 and pTexto[aux] not in strSeparadores:
			aux -= 1
		#
	#
	if pTexto[aux] in strSeparadores:
		while aux >= 0 and pTexto[aux] in strSeparadores:
			aux -= 1
		#
	#
	
	if aux < 0:
		return "None"
	else:
		return corrente(pTexto, aux)
	#
#

def proximo(pTexto, pPosicao):
	strSeparadores = " ,.:;!?"
	aux = pPosicao
	
	if pTexto[aux] not in strSeparadores:
		while aux < len(pTexto) and pTexto[aux] not in strSeparadores:
			aux += 1
		#
	#
	
	if pTexto[aux] in strSeparadores:
		while aux < len(pTexto) and pTexto[aux] in strSeparadores:
			aux += 1
		#
	#
	
	if aux >= len(pTexto):
		return "None"
	else:
		return corrente(pTexto, aux)
	#
#

def uniao(pTexto1, pTexto2):
	lstTexto1 = separaPal(pTexto1)
	lstTexto2 = separaPal(pTexto2)
	u = []
	
	for texto1 in lstTexto1:
		if texto1 not in u:
			u.append(texto1)
		#
	#
	
	for texto2 in lstTexto2:
		if texto2 not in u:
			u.append(texto2)
		#
	#
	
	return u
#	

# Retorna um dicionário com as palavras e a quantidade de vezes q ela apareceu no texto
def geraTabFreq(pTexto):
	lstPalavras = separaPal(pTexto)
	dicPalavras = {}

	for palavra in lstPalavras:
		if palavra not in dicPalavras:
			dicPalavras[palavra] = 1
		else:
			dicPalavras[palavra] += 1
		#
	#
	return dicPalavras
#

# Em números romanos, um algarismo não pode se repetir mais q três vezes ...
def ehRomano(pTexto):
	strNum = "IVXLCDM"
	
	for alg in pTexto:
		if alg not in strNum:
			return False
		#
	#
	return True
#

def codifica(pTexto):
	preposicoes = ['a', 'ante', 'até', 'após', 'com', 'contra','de', 'desde','em','entre','para','per',
	'perante','por','sem','sob','sobre','trás']
	conjuncoes = ['e', 'nem', 'mas também', 'como também', 'bem como', 'mas ainda','mas', 'porém', 'todavia', 'contudo', 'antes']
	artigos = ['o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas']
	strCodificada = ""
	
	for elem in pTexto:
		if elem.lower() in preposicoes:
			strCodificada += 'p'
		elif elem.lower() in artigos:
			strCodificada += 'a'
		elif elem.lower() in conjuncoes:
			strCodificada += 'c'
		elif elem[0].isupper():
			strCodificada += 'M'
		elif elem.isdigit():
			strCodificada += 'N'
		elif elem.islower:
			strCodificada += 'm'
		else:
			strCodificada += elem
		#
	return strCodificada
#

