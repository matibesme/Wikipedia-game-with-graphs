import acciones
import csv
import sys
import funciones




def main():
    
    if len(sys.argv) !=2:
        print("Error de parametros")
        sys.exit(1)

    archivo=sys.argv[1]

    #lectura del archivo
    grafo_wiki=funciones.leerArchivoTsvYCrearGrafo(archivo)
  
    while True:
        
            entrada=input().split()

            if entrada[0]==acciones.COMANDOS[0]:
                acciones.EjecutarListarComandoEImprimirRespuesta()
            elif entrada[0]==acciones.COMANDOS[1]:
                acciones.EjecutarDiametroEImprimirRespuesta(grafo_wiki)
            elif entrada[0]==acciones.COMANDOS[2]:
                en=" ".join(entrada[1:])
                v1,v2=en.split(",")
                acciones.EjecutarCaminoMasCortoEImprimirRespuesta(grafo_wiki,v1,v2)
            elif entrada[0]==acciones.COMANDOS[3]:
                en=" ".join(entrada[1:])
                v1,v2=en.split(",")
                acciones.EjecutarTodosEnRangoEImprimirRespuesta(grafo_wiki,v1,int(v2))
            elif entrada[0]==acciones.COMANDOS[4]:
                if len(entrada) != 2:
                    print("Faltan parametros")
                    continue
                acciones.EjecutarNavPorPrimerLinkEImprimirRespuesta(grafo_wiki,entrada[1])
            elif entrada[0] == acciones.COMANDOS[5]:
                en=" ".join(entrada[1:])
                lista=en.split(",")
                acciones.EjecutarLectura2amEImprimirRespuesta(grafo_wiki, lista)
            elif entrada[0] == acciones.COMANDOS[6]:
                if len(entrada)!=1:
                    en=" ".join(entrada[1:])
                    acciones.EjecutarClusteringEImprimirRespuesta(grafo_wiki,en)
                else:
                    acciones.EjecutarClusteringEImprimirRespuesta(grafo_wiki,None)
                
            else:
                print("No existe el comando")
            

if __name__ == "__main__":
    main()


