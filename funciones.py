from grafo.grafo import *




def leerArchivoTsvYCrearGrafo(nombre_archivo):
    
    vertices=[]
    with open(nombre_archivo,'r') as archivo:
        for linea in archivo:
            componentes=archivo.readline().split("\t")
            vertices.append(componentes[0])
        grafo=Grafo(True, vertices)
        for linea in archivo:
            componentes=archivo.readline().split("\t")
            for componente in componentes[1:]:
                grafo.agregar_arista(componentes[0], componente)
    
    return grafo