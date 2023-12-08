from grafo.grafo import *
from collections import deque



#DIAMETRO 
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
    visitados = {origen: True}
    padres = {origen: None}
    distancias = {origen: 0}
    q = deque()
    q.append(origen)
    while len(q) > 0:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados[w]=True
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
    visitados = {origen: True}
 
    padres = {origen: None}
    distancias = {origen: 0,destino: 0}
    q = deque()
    q.append(origen)
    while len(q) > 0:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados[w]=True
                padres[w] = v
                distancias[w] = distancias[v] + 1
                q.append(w)
                if w == destino:
                    return reconstruir_camino(origen, destino, padres),distancias[destino]
    return None,distancias[destino]

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
    visitados = {vertice:True}
    distancias = {vertice: 0}
    q = deque()
    q.append(vertice)
    while len(q) > 0:
        v = q.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados[w]=True
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
    primer_comp=next(iter(grafo.adyacentes(origen)))
    lista_navegacion.append(primer_comp)
    contador += 1
    if contador == 20:
        return
    navegacion(grafo,  primer_comp, lista_navegacion, contador)

#LECTURA 2AM
def lectura_2am_dfs(grafo, paginas):
    visitados = {}
    set_paginas = {}
    for pagina in paginas:
            set_paginas[pagina]=True
    resultado = []
   
    for v in paginas[::-1]:
        visitados_dfs = {"hay_ciclo": False}
        if v not in visitados:
           _recorrido_dfs(grafo,v,visitados,set_paginas, resultado, visitados_dfs)
           
        if visitados_dfs["hay_ciclo"]:
                return None

    return resultado 

def _recorrido_dfs(grafo,v,visitados,set_paginas,resultado, visitados_dfs):
    visitados_dfs[v] = True
    visitados[v]=True
    ady=grafo.adyacentes(v)
  
  
    for w in ady:
        if w in visitados_dfs:
            visitados_dfs["hay_ciclo"] = True
            return 
        if w not in visitados and w in set_paginas:
            _recorrido_dfs(grafo,w,visitados,set_paginas,resultado,visitados_dfs)
       
    if v in set_paginas:
        resultado.append(v)
        del visitados_dfs[v]


#CLUSTERING
def coeficiente_de_clustering(grafo, pagina=None):
    if pagina is not None:
        return clustering_individual(grafo, pagina)
    
    contador = 0
    total_vertices = len(grafo.obtener_vertices())

    for v in grafo.obtener_vertices():
        contador += clustering_individual(grafo, v)
      
    clustering_promedio = (1/total_vertices) * contador
    return clustering_promedio

def clustering_individual(grafo, vertice):
    grado_salida = grados_de_salida(grafo, vertice)
    if grado_salida < 2:
        return float(0.000)

    contador = 0
    for v in grafo.adyacentes(vertice):
        for w in grafo.adyacentes(vertice):
            if v != w and grafo.estan_unidos(v, w) and v != vertice and w != vertice:
                contador += 1
    clustering_individual = contador / (grado_salida*(grado_salida-1))
    return clustering_individual

def grados_de_salida(grafo,v):
    cont = 0
    for w in grafo.adyacentes(v):
        if w != v:
            cont += 1
    return cont

