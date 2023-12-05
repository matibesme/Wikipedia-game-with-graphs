class Arista:
    def __init__(self, origen, destino, peso = 1):
        self.origen = origen
        self.destino = destino
        self.peso = peso
    
    def obtener_origen(self):
        return self.origen
    
    def obtener_destino(self):
        return self.destino
    
    def obtener_peso(self):
        return self.peso

    def __str__(self):
        return self.obtener_origen() + "--->" + self.obtener_destino()


class Grafo:

    def __init__(self, es_dirigido = False, vertices = []):
        self.dirigido = es_dirigido
        self.vertices = {}
        if len(vertices) != 0:
            for vertice in vertices:
                self.vertices[vertice] = []
    
    def obtener_vertices(self):
        return list(self.vertices.keys())

    def agregar_vertice(self, vertice):
        if vertice in self.vertices:
            raise ValueError(f"Ya hay un vertice {vertice} en el grafo")
        self.vertices[vertice] = []

    def agregar_arista(self, v, w, peso = 1):
        if v not in self.vertices:     
            raise ValueError(f"No hay un vertice {v} en el grafo")
        elif w not in self.vertices:
            raise ValueError(f"No hay un vertice {w} en el grafo")
        if self.estan_unidos(v, w):
            raise ValueError("Ya existe la arista")
        if not self.dirigido:
            arista_wv = Arista(w, v, peso)
            self.vertices[w].append(arista_wv)
        arista_vw = Arista(v, w, peso)
        self.vertices[v].append(arista_vw)

    def estan_unidos(self, v,  w):
        return any(arista.obtener_destino() == w for arista in self.vertices[v])
    
    
    def peso_arista(self, v , w):
        if not self.estan_unidos(v,w):
            raise ValueError(f"No existe la arista entre {v} y {w}")
        for arista in self.vertices[v]:
            if arista.obtener_destino() == w:
                return arista.obtener_peso()
        return
    
            
    def vertice_aleatorio(self):
        if len(self.vertices) == 0:
            raise ValueError("No hay vertices en el grafo")
        return self.obtener_vertices()[0]
    
    def adyacentes(self, vertice):
        res = []
        for arista in self.vertices[vertice]:
            res.append(arista.obtener_destino())
        return res
    
    
    

    def buscar_arista(self, v, w):
        for arista in self.vertices[v]:
            if arista.obtener_destino() == w:
                return arista
        raise ValueError(f"No existe la arista entre {v} y {w}")


        
