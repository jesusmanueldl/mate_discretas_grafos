import pinta #archivo para pintar Grafos (debes definirla)
from class_grafo import Vertice, Arista, Grafo

import igraph as ig
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Calculamos el grado de un vertice, recibe el Grafo y el vertice    
def grado_verice(G:Grafo, vi:Vertice):
    g = 0
    for a in G.A:
        if a.vi.info == vi:
            g+=1
    return g

#Calculamos los vertice adyacentes(vecinos) a un vertice, recibe un Grafo, y un vertice
def vertice_adyacente(G:Grafo, vi:Vertice):
    ady = [] #lista de vertices
    for a in G.A: # [a0, a1] a0.info == vi.info 
        if a.vi.info == vi.info:
            ady +=[a.vf] # ady +=[a.vf.inf]
    #ady.sort()
    return ady

#Hacemos la representcion del grfo con la matriz de adyacencia
def matriz_adyacencia(G):
    mtad =[]
    for v in G.V: #[v1,v2,v3...]
        fila =[]       
        ad = vertice_adyacente(G, v)       
        for a in G.V:            
            if a.info in ad:
                fila +=[1]
            else:
                fila +=[0]
        mtad +=[fila]
    return mtad

'''
Esta funcion vamos a leer un archivo.dat para leer los grafos
el formato del archivo es una lista de la relaciones de cada vertice,
las filas debe coincidir con el total de vertices, es decir el primer nuero de cada fila
pertenece aun vertice del grafo, si no tiene relacion alguna de igual forma se coloca:
|----------| 
|1 3       | 
|2 1 2 3   | 
|3 1 4     | 
|4 1       |
|5         | 
|----------|
'''
def leer_grafo_file(nombre_file, nombre_grafo):
    try:        
        with open(nombre_file, 'r') as archivo:        
            Ar,Vr = [],[]            
            for c in archivo:
                c = c.split()
                cad_1, cad_2 = "",""              
                cad_1 +=str(c[0])
                ar_0 = Vertice(cad_1)                
                Ar +=[ar_0]                
                if c[1:]:                           
                    for ci in range(1,len(c[1:])):                        
                            cad_2 += str(c[ci]) 
                            Vr +=[Arista(ar_0, Vertice(cad_2))]
                            cad_2 =""
                else:
                    Vr +=[Arista(ar_0, Vertice(cad_2))] 
        return Grafo(Ar,Vr,nombre_grafo)  
    except FileNotFoundError:
        print("El archivo no se encontro")

'''
|------------| <vi vf w> el vertice inicial, vertice final y su peso
|1 3 2       | 
|2 1 2 2 3   | <vi vf w vf w
|3 1 4 4 1   | 
|4 1 4       |
|5           | 
|------------|
'''        

def leer_grafop_file(nombre_file, nombre_grafo):
    try:        
        with open(nombre_file, 'r') as archivo:        
            Ar,Vr = [],[]            
            for c in archivo:
                c = c.split()
                cad_1, cad_2 = "",""              
                cad_1 +=c[0]+""
                ar_0 = Vertice(cad_1)                
                Ar +=[ar_0]
                #posicion del sguente vf  [1 2 w 3 w 4 w]
                inc = 0              
                if c[1:]:                           
                    for ci in range(1,len(c[1:]),2):                        
                            cad_2 += str(c[ci])                                   
                            Vr +=[Arista(ar_0, Vertice(cad_2), c[ci+1])]
                            cad_2 =""                         
                else:
                    Vr +=[Arista(ar_0, Vertice(cad_2))] 
        return Grafo(Ar,Vr,nombre_grafo)  
    except FileNotFoundError:
        print("El archivo no se encontro")  

#piinta la Mattriz de adyacencia de un grafo, Recibe una matriz de adyacencia
#pinta_matriz_adyacencia(matriz_adyacencia(g1))
def pinta_matriz_adyacencia(mtady):
    print('\n'.join(map(str, mtady)))

#grado de un vertice de salida para un grafo digrafo
def grado_V_Salida(G:Grafo, vi:Vertice):#grados de vertice de Salida
    cont = 0
    for ai in G.A: # G.A = [[i,f,w],....], ai = [i,f,w]i
        if ai.vi.info == vi.info:
            cont += 1
    return cont

def grado_V_Entrada(G:Grafo, v_i:Vertice): #grados de vertice de entrada
    cont = 0
    for ai in G.A: # G.A = [[i,f,w],....], ai = [i,f,w]i
        if ai.vf.info == v_i.info:
            cont += 1
    return cont

#lista de grados del grafo(susesion grafica de un grafo)
def grados_vertices_salida(G:Grafo):
    return list(map(lambda vi: grado_V_Salida(G,vi), G.V))#[1, 2, 3, 4, 5],

def describe_grafo_dist(G): #describenimos el grafo con ls persos de cada vertice
    return list(map(lambda vi: [vi.info, vi.visitado, vi.dist, list(map(lambda x: x.info, vi.padre))], G.V))

def busca_vertice(G:Grafo,info: int)->Vertice: #buscamos un vertice por su info en el grafo y devolvemos ese vertice
    for v in  G.V:
        if v.info == info:
            return v
    return None

#Busqueda en amplitud para ARBOLES
def BFS(G:Grafo, vi:Vertice):
    vi.visitado = True
    vi.distancia = 0
    Q = []
    Qresult = []#lista resultante     
    Q += [vi]
    Qresult +=[vi]   
    while Q:
        u = Q.pop(0)
        for v in vertice_adyacente(G,u): #[1,4,5,] [Vert en formato Vertice]                         
            if not v.visitado:           
                v.visitado = True
                v.distancia = u.distancia + 1
                Q += [v] 
                Qresult += [v]                
    return list(map(lambda x: [x.info, "d: "+str(x.distancia)], Qresult))

def pos_vert(G:Grafo, vi: Vertice): #calculamos la posicion de un vertice en el grafo
        pos = 0
        for v in G.V:
            if v.info == vi.info:                
                    return pos          
            pos +=1
        return -1

def pos_arista(G:Grafo, A: Arista): #calculamos la posicion de una arista en el grafo
        pos = 0
        for a in G.A:
            if a.vi.info == A.vi.info and  a.vf.info == A.vf.info:               
                return pos          
            pos +=1
        return -1


def dist_min(Q): #calculamos cual de los vertice de la cola Q es mas pequeño en uento a su peso
    vi = Q[0]
    for vx in Q:
        if vx.dist < vi.dist:
            vi = vx
    return vi

def peso(G, vi, vf): #calculamo el peso de un vertice a otro
    for a in G.A:
        if a.vi.info == vi.info and a.vf.info == vf.info:
            return a.w

#algoritmo de busqueda en profundidad
def DFS(G:Grafo, vi:Vertice, vf:Vertice):
    Q = []
    Q += [vi]
    G.V[pos_vert(G,vi)].visitado = True
    while Q:
        vAct = Q.pop(0)
        if vAct.info == vf.info:
            return True
        for w in vertice_adyacente(G, vAct):
            if not w.visitado:
                Q +=[w]
                G.V[pos_vert(G,w)].visitado = True
    return False    

def dijkstra(G:Grafo, vi:Vertice):
    G.V[pos_vert(G,vi)].dist = 0  # el vertice actual
    Q = [G.V[pos_vert(G,vi)]] # una cola de vertices adyacetes con pesos 
    while Q: #mientras haya vertices adyacentes en la cola
        u = dist_min(Q) #calculamos de todos los vertices en Q cual es el minimo en sus distancias   
        G.V[pos_vert(G,u)].visitado = True #marcamos como visitado el vertice por el que empezamo
        Q.remove(u) #lo sacamos de la cola     
        for vr_ad in vertice_adyacente(G,G.V[pos_vert(G,u)]): #bucamos los adyacentes e vi, el certice en de inicio
            if not G.V[pos_vert(G,vr_ad)].visitado: #comprovamos que los adyacentes ho hayan sido visistado
                if G.V[pos_vert(G,vr_ad)].dist > round(G.V[pos_vert(G,u)].dist + peso(G, G.V[pos_vert(G,u)], G.V[pos_vert(G,vr_ad)]),2): # calculamos cuanto nos cuenta de ir del vertice inicial al primero adyacente     
                    G.V[pos_vert(G,vr_ad)].dist = round(G.V[pos_vert(G,u)].dist + peso(G, G.V[pos_vert(G,u)], G.V[pos_vert(G,vr_ad)]),2) #si sale mejor calculamos su distancia
                    G.V[pos_vert(G,vr_ad)].padre += [G.V[pos_vert(G,u)]] #lo cargamos auna lista del cual llego                
                    Q += [G.V[pos_vert(G,vr_ad)]] #guardamos el adyacente que ha sido modificado
                    
                    #print([u.info, u.visitado, u.dist, list(map(lambda x: x.info, u.padre))])
        # list(map(lambda vij: [vij.info, vij.visitado, vij.dist, vij.padre], G.V))

def Floyd_Warshall(G:Grafo):
    mad_pesos = []    
    for vi in G.V:
        fila = []
        for vj in G.V:
            if vi.info == vj.info:
                fila += [0]               
            else:
                pos_ar = pos_arista(G,Arista(G.V[pos_vert(G,vi)], G.V[pos_vert(G,vj)]))
                if pos_ar != -1:
                    fila += [G.A[pos_ar].w]
                else:
                    fila += [float('+inf')]
        mad_pesos += [fila]

        n = len(mad_pesos)
        D = [row[:] for row in mad_pesos]
        for k in range(0,n): #calculamos las distancias cortas pasando por k
            for i in range(0,n): #aqui vamos a iterar sobre los verticces fila
                if i != k:
                    for j in range(0,n):#aqui vamos a iterar sobre los verticces columna
                        if j != k:
                            dt = round(D[i][k] + D[k][j],2) #calculamos cuanto cuesta ir de i a j pasando por k
                            if D[i][j] > dt: #si es menor ese valor que dij lo cambiamos
                                D[i][j] = dt
    return mad_pesos,D

def buscar_vf(L, c): #busca el vertice final en la lista de vertices con sus pesos
     for li in L:
        if li[0] == c:
           return li[3][len(li[3])-1], li[0]

def camino_corto_vi_vf(G:Grafo, vi:Vertice, vf:Vertice): #calcula el camino mas carto de ir de vi a vf usando dijkstra
    camino = []
    dijkstra(G,vi)
    dist_dijk = list(map(lambda vi: [vi.info, vi.visitado, vi.dist, list(map(lambda x: x.info, vi.padre))], G.V))
    ci = vf.info
    while ci != vi.info:
        ci,ca = buscar_vf(dist_dijk, ci)
        camino.insert(0, ca)
    camino.insert(0,vi.info)
    return camino

def cerrar_calle(G:Grafo, vi, vf):
    G.A[pos_arista(G, Arista(busca_vertice(G,vi),busca_vertice(G,vf)))].w = float('+inf')




def pintaGP(G:Grafo):
    n_vertices = len(G.V)
    edges = list(map(lambda x: [x.vi.info, x.vf.info], G.A))  
    g = ig.Graph(n_vertices, edges, directed=True)    
    g.es["weight"] = list(map(lambda x: x.w, G.A))    
    vertices_info = list(map(lambda x: x.info, G.V)) 
    fig, ax = plt.subplots()
    ig.plot(
        g, 
        target= ax,
        layout="auto",
        vertex_color="lightgreen", 
        edge_curved=False, 
        vertex_label=vertices_info,
        edge_label=g.es["weight"],
        edge_color='#666',
        edge_align_label=False,
        edge_label_size=6,
        edge_width=0.5,
        vertex_size=20,
        vertex_label_size=9.5
    )
    plt.show()
    
        
#Definicion de los Vertices        
v1 = Vertice(1)
v2 = Vertice(2)
v3 = Vertice(3)
v4 = Vertice(4)
v5 = Vertice(5)
v6 = Vertice(6)
v7 = Vertice(7)

#conjunto de Vertices
lv = [v1,v2,v3,v4,v5,v6,v7] #A = [1,2,3,4,5,6]

#Definicion de las Aristas
a1 = Arista(v1,v2)
a2 = Arista(v2,v3)
a3 = Arista(v2,v4)
a4 = Arista(v1,v5)
a5 = Arista(v5,v6)
a6 = Arista(v6,v7)

#Conjunto de Aristas
la = [a1,a2,a3,a4,a5,a6]

#Definicion del Grafo

g1 = Grafo(lv,la,"G1")
#print(g1.inf)
'''
print("grados de V1 saldia: "+str(grado_V_Salida(g1, v1)))
print("grados de V1 entrada: "+str(grado_V_Entrada(g1, v1)))
print("grados de los vertices del Grafo: "+str(grados_vertices_salida(g1)))

pinta.pinta_grafop(g1, "G1", "circo",True)


'''
#print(BFS(g1, v1))
#vertice 
#v = 3
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
#Gf=leer_grafop_file("g2p.dat", "G2P")
#print(Gf.inf)
#pinta.pinta_grafop(Gf, "G2", "circo",True)
#print(matriz_adyacencia(leer_grafo_file("g.dat", "G2")))
#pinta_matriz_adyacencia(matriz_adyacencia(leer_grafo_file("g1.dat", "G2")))
colonia = leer_grafop_file("colonia.dat", "Cunducan")
coordenadas = ('1 [pos="10.99,-23.18!"]\n2 [pos="5.95,-21.62!"]\n3 [pos="1.47,-19.64!"]\n4 [pos="1.31,-16.40!"]\n5 [pos="4.61,-3.70!"]\n'
        '6 [pos="20.83,-1.33!"]\n7 [pos="31.13,-4.30!"]\n8 [pos="33.23,-5.51!"]\n9 [pos="33.83,-7.17!"]\n10 [pos="34.49,-8.69!"]\n'
        '11 [pos="35.44,-10.32!"]\n12 [pos="36.18,-11.60!"]\n13 [pos="37.32,-13.10!"]\n14 [pos="32.62,-14.55!"]\n15 [pos="28.62,-15.86!"]\n'
        '16 [pos="24.42,-17.62!"]\n17 [pos="20.60,-19.31!"]\n18 [pos="15.43,-18.98!"]\n19 [pos="7.42,-16.21!"]\n20 [pos="5.44,-16.09!"]\n'
        '21 [pos="8.11,-6.68!"]\n22 [pos="14.05,-4.98!"]\n23 [pos="21.21,-4.02!"]\n24 [pos="31.14,-8.12!"]\n25 [pos="31.56,-10.00!"]\n'
        '26 [pos="32.10,-11.50!"]\n27 [pos="32.28,-12.95!"]\n28 [pos="28.16,-14.23!"]\n29 [pos="23.74,-15.94!"]\n30 [pos="19.76,-17.96!"]\n'
        '31 [pos="18.74,-16.36!"]\n32 [pos="10.50,-13.42!"]\n33 [pos="10.14,-11.32!"]\n34 [pos="8.54,-8.38!"]\n35 [pos="14.24,-6.97!"]\n36 [pos="17.56,-7.31!"]\n'
        '37 [pos="21.54,-7.19!"]\n38 [pos="27.78,-7.81!"]\n39 [pos="28.78,-11.41!"]\n40 [pos="27.48,-12.71!"]\n41 [pos="23.30,-13.95!"]\n42 [pos="20.54,-14.55!"]\n'
        '43 [pos="12.78,-12.75!"]\n44 [pos="14.74,-10.13!"]\n45 [pos="17.62,-10.17!"]\n46 [pos="21.92,-10.51!"]\n47 [pos="23.08,-11.77!"]\n'
        '48 [pos="21.16,-11.67!"]\n49 [pos="17.60,-11.87!"]\n')
#-------------floyd----
#g001 = leer_grafop_file("g001.dat", "GF")
#mad_p, mad_d = Floyd_Warshall(g001)
#mad_p, mad_d = Floyd_Warshall(colonia)
#print('\n'.join(map(str, mad_p))) 
#print('---------FW-----------')
#print('\n'.join(map(str, mad_d)))  #esto es para floid-warshall
#pinta.pinta_grafo(g001, "Floyd_Warshall", "dot",False,True)
#print(colonia.info)
#dijkstra(g001, busca_vertice(g001,1))

## EJERCICO DE TAPAR CALLES PARA CALCULAR OTRA OPCION  #############
#cerrar_calle(colonia, 1, 18)
#cerrar_calle(colonia, 1, 17)
#cerrar_calle(colonia, 6, 7)
#corto = camino_corto_vi_vf(colonia, busca_vertice(colonia,1), busca_vertice(colonia,7)) 
#print(corto)
#pinta.pinta_grafo(colonia, "Cunduacan1", "neato",True,True, corto, coordenadas)

###################################33
#print(describe_grafo_dist(g001))
#print(DFS(colonia, busca_vertice(colonia,1), busca_vertice(colonia,7)))
'''
# Carga la imagen desde un archivo
imagen = mpimg.imread('Cunduacan.png')
# Visualiza la imagen
plt.imshow(imagen)
# Opcionalmente, puedes agregar un título a la figura
plt.title('Camino más corto: '+ corto)
# Muestra la imagen en una ventana emergente
plt.show()
'''

#dijkstra(colonia, busca_vertice(colonia,1))
#print(describe_grafo_dist(colonia))
#camino = camino_corto_vi_vf(colonia, busca_vertice(colonia,1), busca_vertice(colonia,7))
#print(list(map(lambda i,f: [Arista(Vertice(i),Vertice(f))], camino[:-1], camino[1:])))
#mad_p = Floyd_Warshall(colonia)
#print('\n'.join(map(str, mad_p))) 
#pinta.pinta_grafo(leer_grafop_file("colonia.dat", "colonia"), "colonia", "dot",True, True)
#pinta.pinta_grafop(g1, "BFS", "dot",False)
#pinta.pinta_grafo(colonia, "Cunducan", "dot",True,True)


#print(describe_grafo_dist(colonia))
#gf1 = leer_grafop_file("g001.dat", "GF")
#pintaGP(gf1)
#print(camino_corto_vi_vf(gf1, busca_vertice(gf1,1), busca_vertice(gf1,6)))
#pinta.pinta_grafo(gf1, "gf1","dot",False,True)

#gpneg = leer_grafop_file("grafopnegativo.dat", "gpneg")
#mad_p, mad_d = Floyd_Warshall(gpneg)
#print('\n'.join(map(str, mad_p))) 
#print('---------FW-----------')
#print('\n'.join(map(str, mad_d)))  #esto es para floid-warshall
#pinta.pinta_grafo(gpneg, "gpneg","circo",False,True)

