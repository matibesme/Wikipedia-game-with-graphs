import acciones
import csv
import sys
import funciones




def main():
 
    if len(sys.argv) !=2:
        print("Error de parametros")
        sys.exit(1)

    archivo=sys.argv[2]

    #lectura del archivo
    grafo_wiki=funciones.leerArchivoTsvYCrearGrafo(archivo)
    #comandos

    while True:
        
            entrada=input().split()

            if entrada[0]==acciones.COMANDOS[0]:
                acciones.EjecutarListarComandoEImprimirRespuesta()
            elif entrada[0]==acciones.COMANDOS[1]:
                acciones.EjecutarDiametroEImprimirRespuesta(grafo_wiki)
            elif entrada[0]==acciones.COMANDOS[2]:
                if len(entrada)!=3:
                    print("Faltan parametros")
                    continue
                acciones.EjecutarCaminoMasCortoEImprimirRespuesta(grafo_wiki,entrada[1],entrada[2])
            elif entrada==acciones.COMANDOS[3]:
                if len(entrada)!=3:
                    print("Faltan parametros")
                    continue
                acciones.EjecutarTodosEnRangoEImprimirRespuesta(grafo_wiki,entrada[1],int(entrada[2]))
            elif entrada[0]==acciones.COMANDOS[4]:
                if len(entrada) != 2:
                    print("Faltan parametros")
                    continue
                acciones.EjecutarNavPorPrimerLinkEImprimirRespuesta(grafo_wiki,entrada[1])
            elif entrada[0] == acciones.COMANDOS[5]:
                if len(entrada) < 2:
                    print("Faltan parametros")
                    continue
                acciones.EjecutarLectura2amEImprimirRespuesta(grafo_wiki, entrada[1:])

