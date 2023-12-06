from biblioteca import *

COMANDOS=["listar_operaciones","diametro","camino","rango","navegacion","lectura"]

def EjecutarCaminoMasCortoEImprimirRespuesta(grafo, origen, destino):
    lista_camino, costo = camino_mas_corto(grafo, origen, destino)
    if lista_camino is None:
        print("No se encontro recorrido")
        return
    camino_str = " -> ".join(lista_camino)
    print(camino_str)
    print(f"Costo: {costo}")

def EjecutarDiametroEImprimirRespuesta(grafo):
    lista_diametro, distancia_diametro = obtener_diametro(grafo)
    diametro_str = " -> ".join(lista_diametro)
    print(diametro_str)
    print(f"Costo: {distancia_diametro}")

def EjecutarTodosEnRangoEImprimirRespuesta(grafo, pagina, n):
    contador = rango(grafo, pagina, n)
    print(contador)

def EjecutarNavPorPrimerLinkEImprimirRespuesta(grafo, origen):
    lista_navegacion = navegacion_primer_link(grafo, origen)
    navegacion_str = " -> ".join(lista_navegacion)
    print(navegacion_str)
    
def EjecutarListarComandoEImprimirRespuesta():
    cadena = "\n".join(COMANDOS[1:])
    print(cadena)

def EjecutarLectura2amEImprimirRespuesta(grafo, lista_paginas):
    resultado = lectura_2am_dfs(grafo, lista_paginas)
    if resultado is None:
        print("No existe forma de leer las paginas en orden")
        return
    resultado_str = ", ".join(resultado)
    print(resultado_str)
