#import pinta #archivo para pintar Grafos (debes definirla)


#definimos un Vertice
class Vertice:
    def __init__(self,info):
        if isinstance(info, str):
            self.inf = str(info)
        else:
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

#Calculamos el grado de un vertice, recibe el Grafo y el vertice    
def grado_verice(G, v):
    g = 0
    for a in G.A:
        if a.vi.inf == v:
            g+=1
    return g

#Calculamos los vertice adyacentes(vecinos) a un vertice, recibe un Grafo, y un vertice
def verice_adyacente(G, v):
    ady = []
    for a in G.A:
        if a.vi.inf == v:
            ady +=[a.vf.inf]
    ady.sort()
    return ady

#Hacemos la representcion del grfo con la matriz de adyacencia
def matriz_adyacencia(G):
    mtad =[]
    for v in G.V:
        fila =[]       
        ad = verice_adyacente(G, v.inf)       
        for a in G.V:            
            if a.inf in ad:
                fila +=[1]
            else:
                fila +=[0]
        mtad +=[fila]
    return mtad

'''
Esta funcion vamos a leer un archivo.dat para leer los grafos
el formato del archivo es una lista de la relaciones de cada vertice,
las filas debe coincidir con el total de vertices:
|----------| 
|1 2 3 4   | 
|2 2 3     | 
|3 1 4     | 
|4 1       | ;<----"sin salto de linea al final de la ultima lista"
|----------|
'''
def leer_grafo_file(nombre_file, nombre_grafo):
    try:
        with open(nombre_file, 'r') as archivo:        
            Ar = []
            Vr = []
            for c in archivo:
                cad_1 =""
                for ci in c:
                    if ci != ' ' and ci != '\n':
                        cad_1 += ci
                    else:
                        break
                Ar +=[Vertice(cad_1)] 
                cad_2 =""               
                for ci in c[len(cad_1)+1:]:
                    if ci != ' ' and ci != '\n':
                        cad_2 += ci                 
                    elif cad_2 != "":
                        Vr +=[Arista(Vertice(cad_1), Vertice(cad_2))]
                        cad_2 =""                    
            Vr +=[Arista(Vertice(cad_1), Vertice(cad_2))] ##si el achivo no tiene ultima linea
        return Grafo(Ar,Vr,nombre_grafo)  
    except FileNotFoundError:
        print("El archivo no se encontro") 

#piinta la Mattriz de adyacencia de un grafo, Recibe una matriz de adyacencia
#pinta_matriz_adyacencia(matriz_adyacencia(g1))
def pinta_matriz_adyacencia(mtady):
    for m in mtady:
        print(m)
        


        
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

#Conjunto de Aristas
la = [a1,a2,a3,a4,a5,a6,a7]

#Definicion del Grafo
#g1 = Grafo(lv,la,"G1")
#print(g1.inf)

#vertice 
v = 3
#print(f'Grado del vertice {v}: '+str(grado_verice(g1,v)))
#print(f'Vertices adyacente/incidente de {v}: '+str(verice_adyacente(g1,v)))
#mtr = matriz_adyacencia(g1)
#print("Matriz de Adyacencia")
#for m in mtr:
#    print(m)

#print(archivo.read())
#Visualizamos el Grafo, 
#pinta.pinta_grafo(g1,"G1") #define esta funcion
#print(leer_grafo_file("g.dat", "G2").inf)
Gf=leer_grafo_file("g.dat", "G2")
print(Gf.inf)
#print(matriz_adyacencia(leer_grafo_file("g.dat", "G2")))
pinta_matriz_adyacencia(matriz_adyacencia(leer_grafo_file("g.dat", "G2")))
#pinta.pinta_grafo(leer_grafo_file("g.dat", "G2"), "G2")