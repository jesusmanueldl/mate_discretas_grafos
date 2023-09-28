#definimos una arista
class Vertice:
    def __init__(self,info):
        self.inf = info



class Arista:
    def __init__(self, vi, vf):
        self.vi = vi
        self.vf = vf
        self.inf = [self.vi.inf,self.vf.inf]
        
class Grafo:
    def __init__(self, V, A, nom):
        self.V = V
        self.A = A
        self.nombre = nom
        self.inf = [list(map(lambda x: x.inf, self.V)),list(map(lambda x: x.inf, self.A)),self.nombre]



v1 = Vertice(1)
v2 = Vertice(2)
v3 = Vertice(3)
lv = [v1,v2,v3]

a1 = Arista(v1,v2)
a2 = Arista(v1,v3)
la = [a1,a2]

g1 = Grafo(lv,la,"G1")


