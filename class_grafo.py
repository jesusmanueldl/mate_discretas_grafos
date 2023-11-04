#definimos un Vertice
class Vertice:
    def __init__(self,info):                    
        try:
            self.info = int(info)
        except ValueError:
            try:
                self.info = float(info)
            except ValueError:
                if isinstance(info,str):
                    self.info = info
        self.visitado = False
        self.dist = float('+inf')   #lo que cuesta llegar a el Vertice vi
        self.padre = []     
        

#definimos una Arista
class Arista:
    def __init__(self, vi, vf, weight = float('+inf')):
        self.vi = vi
        self.vf = vf
        if weight == float('+inf'):
            self.weight = weight #ponderdo de la arista
        else:
            if '.' in str(weight):
                self.weight = float(weight)
            else:                
                self.weight = int(weight)           
        self.info = [self.vi.info, self.vf.info, self.weight] #informacion de la arista
  

#definimos un Grafo
class Grafo:
    def __init__(self, V, A, nombre):
        self.V = V
        self.A = A
        self.nombre = nombre
        self.info = [list(map(lambda x: x.info, self.V)),
                    list(map(lambda x: x.info, self.A)),self.nombre]