from class_grafo import Vertice, Arista, Grafo
import subprocess
import tkinter as tk #intalar esta libreria
from PIL import Image, ImageTk #instalar esta libreria
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def pos_arista(GA, A): #calculamos la posicion de una arista en el grafo
    pos = 0
    for a in GA:
        if a.vi.info == A.vi.info and a.vf.info == A.vf.info:               
            return pos          
        pos +=1
    return -1

def pos_vert(G, vi): #calculamos la posicion de un vertice en el grafo
    pos = 0
    for v in G.V:
        if v.info == vi.info:                
                return pos          
        pos +=1
    return -1

def pos_aris_en_aris(a,B): #calculamos la posicion de un vertice en el grafo
    pos = 0       
    for b in B:
        if a.vi.info == b.vi.info and a.vf.info == b.vf.info:                            
            return pos          
        pos +=1
    return -1

def pinta_grafo(G, nombre="grafo", layout="circo", img_hd=False, p = False, camino=[]): #layout : circo, dot, fdp, neato, osage, twopi
    Q = []
    hay_camino = False
    if camino:
        LC = list(map(lambda i,f: Arista(Vertice(i),Vertice(f)), camino[:-1], camino[1:]))
        hay_camino = True         

    with open('grafo.dot', 'w') as archivo:
        archivo.write('digraph G\n{\n\tnode [shape=circle];\n\tlayout='+layout+';\n\tsize="6,6";\n\trankdir=LR;\n')
        for a in G.A:
            if str(a.vf.info) != "":
                if p:                    
                    if pos_arista(G.A, Arista(a.vf, a.vi)) != -1:
                        if hay_camino:
                            if pos_aris_en_aris(Arista(a.vi, a.vf),LC) != -1:
                                archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '[fontcolor=blue label='+str(a.w)+',fontcolor="red",fontsize="25", color="red", penwidth=2.0]\n')
                            elif pos_aris_en_aris(Arista(a.vf, a.vi),LC) != -1:
                                archivo.write('\t'+str(a.vf.info) + ' -> ' + str(a.vi.info) + '[fontcolor=blue label='+str(a.w)+',fontcolor="red",fontsize="25", color="red", penwidth=2.0]\n')
                            else:                                                                            
                                archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '[fontcolor=blue label='+str(a.w)+', dir=both]\n')
                        else:                                                                            
                            archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '[fontcolor=blue label='+str(a.w)+', dir=both]\n')
                        #if pos_aris_en_aris(Arista(a.vf, a.vi),LC) == -1:
                        G.A.pop(pos_arista(G.A, Arista(a.vf, a.vi)))                                          
                    else:
                        if hay_camino:
                            if pos_aris_en_aris(Arista(a.vi, a.vf),LC) != -1:
                                archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '[fontcolor=blue label='+str(a.w)+',fontcolor="red",fontsize="25", color="red", penwidth=2.0]\n')
                            else:
                                archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '[fontcolor=blue label='+str(a.w)+']\n')
                        else:
                            archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '[fontcolor=blue label='+str(a.w)+']\n')
                         
                else:
                    archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '\n')
            else:
                 archivo.write('\t'+str(a.vi.info) +'\n')
        archivo.write('\tlabel="'+nombre+'"\n}')
    if img_hd:
        comando = 'dot -Tpng -Gdpi=300 -o '+nombre+'.png grafo.dot'
    else:
         comando = 'dot -Tpng -o '+nombre+'.png grafo.dot'    
    subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    showGraph(nombre)

def showGraph(nombre_img):
    imagen = mpimg.imread(nombre_img+'.png')
    # Visualiza la imagen
    plt.imshow(imagen)
    # Opcionalmente, puedes agregar un título a la figura
    plt.title(nombre_img)    
    # Muestra la imagen en una ventana emergente
    plt.show()
    '''
    ventana = tk.Tk()
    ventana.title("Visor de Imagen")
    ruta_imagen = nombre_img+'.png'
    imagen = Image.open(ruta_imagen)
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
    etiqueta_imagen.pack()
    ventana.mainloop()
    '''
