import copy

lista = []

def adiciona_ponto(x, y, r, g, b, nome = '',x0 = 0,y0=0):
    global lista
    lista = lista + [(x, y, r, g, b, nome,x0,y0)]

def limpa_lista():
    global lista
    lista = []

def pega_lista():
    global lista
    return copy.deepcopy(lista)

