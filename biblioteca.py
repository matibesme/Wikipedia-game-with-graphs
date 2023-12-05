from grafo.grafo import *
from collections import deque
#DIAMETROy 
def obtener_diametro(grafo):
    lista_diametro = []
    distancia_diametro = 0
    for v in grafo.obtener_vertices():
        camino_mayor, distancia = mayor_distancia_desde_v(grafo, v)
        if distancia > distancia_diametro:
            distancia_diametro = distancia
            lista_diametro = camino_mayor
    return lista_diametro, distancia_diametro
    
def mayor_distancia_desde_v(grafo, origen):
    visitados = set(origen)
    padres = {origen: None}
    distancias = {origen: 0}
    q = deque()
    while len(q) > 0:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                padres[w] = v
                distancias[w] = distancias[v] + 1
                q.append(w)
    v_mas_lejano = origen
    for vertice, distancia in distancias.items():
        if distancia > distancias[v_mas_lejano]:
            v_mas_lejano = vertice
    lista_camino = reconstruir_camino(origen, v_mas_lejano, padres)
    return lista_camino, distancias[v_mas_lejano]

#CAMINO MAS CORTO
def camino_mas_corto(grafo, origen, destino):
    visitados = set(origen)
    padres = {origen: None}
    distancias = {origen: 0}
    q = deque()
    while len(q) > 0:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                padres[w] = v
                distancias[w] = distancias[v] + 1
                q.append(w)
                if w == destino:
                    break
    if destino not in visitados:
        return None
    reconstruir_camino(origen, destino, padres, distancias)

def reconstruir_camino(origen, destino, padres):
    lista_camino = []
    hijo = destino
    while hijo != origen:
        lista_camino.append(hijo)
        hijo = padres[hijo]
    lista_camino.append(origen)
    lista_camino = lista_camino[::-1]
    return lista_camino

#TODOS EN RANGO
def rango(grafo, vertice, n):
    visitados = set(vertice)
    distancias = {vertice: 0}
    q = deque()
    while len(q) > 0:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                distancias[w] = distancias[v] + 1
                q.append(w)
    contador = 0
    for distancia in distancias.values():
        if distancia == n:
            contador += 1
    return contador 


#NAVEGACION POR PRIMER LINK
def navegacion_primer_link(grafo, origen):
    lista_navegacion = [origen]
    contador = 0
    navegacion(grafo, origen, lista_navegacion, contador)
    return lista_navegacion

def navegacion(grafo, origen, lista_navegacion, contador):
    if len(grafo.adyacentes(origen)) == 0:
        return
    lista_navegacion.append(grafo.adyacentes(origen)[0])
    contador += 1
    if contador == 20:
        return
    navegacion(grafo, grafo.adyacentes(origen)[0], lista_navegacion, contador)



def lectura_2_am(grafo,lista_paginas):
    set_paginas=set()
    visitados=set()
    lista=[]
    for v in lista_paginas:
        set_paginas.add(v)
    
    entradas = grados_entrada_paginas(grafo, lista_paginas, set_paginas)
    q=deque()
    for vertice, valor in entradas.items():
        if valor == 0:
            q.append(vertice)
            visitados.add(vertice)
    while len(q) > 0:
        v=q.popleft()
        lista.append(v)
        for w in grafo.adyacentes(v):
            if w in set_paginas:
                if w in visitados:
                    return None
                entradas[w]-=1
                if entradas[w]==0:
                    visitados.add(w)
                    q.append(w)
    return lista[::-1]
    

def grados_entrada_paginas(grafo, lista_paginas, set_paginas):
    entradas = {}
    for v in lista_paginas:
        entradas[v] = 0
    for v in lista_paginas:
        for w in grafo.adyacentes(v):
            if w in set_paginas:
                entradas[w] += 1
    return entradas

    


   
def coeficiente_de_clustering(grafo,pagina):
    salida=len(grafo.adyacentes(pagina))

    if pagina is not None:
        return clustering_individual(grafo,pagina)
    contador = 0
    for v in grafo.obtener_vertices():
        contador += clustering_individual(grafo, v)
    return (1/len(grafo.obtener_vertices())) * contador
    
    

def clustering_individual(grafo, pagina):
    salida=len(grafo.adyacentes(pagina))
    if len(salida) < 2:
        return 0
    contador=salida
    for v in grafo.adyacentes(pagina):
        if grafo.estan_unidos(v,pagina):
            contador+=1
    return contador/(salida*(salida-1))
        









