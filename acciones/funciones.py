from grafo.grafo import *




def leerArchivoTsvYCrearGrafo(nombre_archivo):
    with open(nombre_archivo,'r') as archivo:
        vertices = []
        for linea in archivo:
            componentes=linea.strip().split("\t")
            vertices.append(componentes[0])
        grafo=Grafo(True,vertices)

    
    
    with open(nombre_archivo,'r') as archivo:
        
        for linea in archivo:
            componentes=linea.strip().split("\t")
            for componente in componentes[1:]:
                if not grafo.estan_unidos(componentes[0],componente):
                    grafo.agregar_arista(componentes[0], componente)


    return grafo



def juntarParametros(lista):
    parametros=" ".join(lista)
    return parametros