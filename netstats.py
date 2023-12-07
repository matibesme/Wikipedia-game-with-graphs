#!/usr/bin/python3
from acciones.acciones import *
import sys
from acciones.funciones import *





def main():
    
    if len(sys.argv) !=2:
        print("Error de parametros")
        sys.exit(1)

    archivo=sys.argv[1]

    #lectura del archivo
    grafo_wiki=leerArchivoTsvYCrearGrafo(archivo)
  
    while True:
        
            entrada=input().split()

            if entrada[0]==COMANDOS[0]:
                EjecutarListarComandoEImprimirRespuesta()
            elif entrada[0]==COMANDOS[1]:
                EjecutarDiametroEImprimirRespuesta(grafo_wiki)
            elif entrada[0]==COMANDOS[2]:
                en=" ".join(entrada[1:])
                v1,v2=en.split(",")
                EjecutarCaminoMasCortoEImprimirRespuesta(grafo_wiki,v1,v2)
            elif entrada[0]==COMANDOS[3]:
                en=" ".join(entrada[1:])
                v1,v2=en.split(",")
                EjecutarTodosEnRangoEImprimirRespuesta(grafo_wiki,v1,int(v2))
            elif entrada[0]==COMANDOS[4]:
                if len(entrada) != 2:
                    print("Faltan parametros")
                    continue
                EjecutarNavPorPrimerLinkEImprimirRespuesta(grafo_wiki,entrada[1])
            elif entrada[0] == COMANDOS[5]:
                en=" ".join(entrada[1:])
                lista=en.split(",")
                EjecutarLectura2amEImprimirRespuesta(grafo_wiki, lista)
            elif entrada[0] == COMANDOS[6]:
                if len(entrada)!=1:
                    en=" ".join(entrada[1:])
                    EjecutarClusteringEImprimirRespuesta(grafo_wiki,en)
                else:
                    EjecutarClusteringEImprimirRespuesta(grafo_wiki,None)
                
            else:
                print("No existe el comando")
            

if __name__ == "__main__":
    main()


