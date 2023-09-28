#import pinta #archivo para pintar Grafos (debes definirla)


#definimos un Vertice
class Vertice:
    def __init__(self,info):
        self.inf = info

#definimos una Arista
class Arista:
    def __init__(self, vi, vf):
        self.vi = vi
        self.vf = vf
        self.inf = [self.vi.inf,self.vf.inf]

#definimos un Grafo
class Grafo:
    def __init__(self, V, A, nombre):
        self.V = V
        self.A = A
        self.nombre = nombre
        self.inf = [list(map(lambda x: x.inf, self.V)),list(map(lambda x: x.inf, self.A)),self.nombre]
        
        
#Definicion de los Vertices        
v1 = Vertice(1)
v2 = Vertice(2)
v3 = Vertice(3)
v4 = Vertice(4)
v5 = Vertice(5)
#conjunto de Vertices
lv = [v1,v2,v3,v4,v5] 

#Definicion de las Aristas
a1 = Arista(v1,v2)
a2 = Arista(v1,v5)
a3 = Arista(v3,v4)
a4 = Arista(v5,v1)
a5 = Arista(v5,v2)
a6 = Arista(v3,v2)
a7 = Arista(v3,v1)
a8 = Arista(v4,v5)
#Conjunto de Aristas
la = [a1,a2,a3,a4,a5,a6,a7,a8]

#Definicion del Grafo
g1 = Grafo(lv,la,"G1")
print(g1.inf)

#Visualizamos el Grafo, 
#pinta.pinta_grafo(g1,"G1") #define esta funcion


