import copy

lista = []

def adiciona_ponto(x, y, r, g, b, nome = ''):
	global lista
	lista = lista + [(x, y, r, g, b, nome)]

def limpa_lista():
	global lista
	lista = []

def pega_lista():
	global lista
	return copy.deepcopy(lista)

