from class_grafo import Vertice, Arista, Grafo
import subprocess
import tkinter as tk #intalar esta libreria
from PIL import Image, ImageTk #instalar esta libreria
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

coordenadas = []

def pos_arista(GA, A): #calculamos la posicion de una arista en el grafo
    pos = 0
    for a in GA:
        if a.vi.info == A.vi.info and a.vf.info == A.vf.info and a.weight == A.weight:               
            return pos          
        pos +=1
    return -1

def pos_arista_sin_peso(GA, A): #calculamos la posicion de una arista en el grafo
    pos = 0
    for a in GA:
        if a.vi.info == A.vi.info and a.vf.info == A.vf.info:               
            return pos          
        pos +=1
    return -1

def pos_vert(G:Grafo, vi:Vertice): #calculamos la posicion de un vertice en el grafo
    pos = 0
    for v in G.V:
        if v.info == vi.info:                
                return pos          
        pos +=1
    return -1

def pos_aris_en_aris(a:Arista,B:list[Arista]): #calculamos la posicion de un vertice en el grafo
    pos = 0       
    for b in B:
        if a.vi.info == b.vi.info and a.vf.info == b.vf.info and a.weight == b.weight:                            
            return pos          
        pos +=1
    return -1

def pinta_grafo(G, nombre="grafo", layout="circo", img_hd=False, p = False, camino=[], coordenadas="", font_size_label=15): #layout : circo, dot, fdp, neato, osage, twopi
    Q = []
    if camino: #si hay caminos en la lista, los paso a una lista de arista 
        LC = list(map(lambda i,f: G.A[pos_arista_sin_peso(G.A, Arista(Vertice(i), Vertice(f)))], camino[:-1], camino[1:]))       
    #style=filled, color="#51c46b", fontcolor="white", fontname="Impact"
    with open('grafo.dot', 'w') as archivo:
        archivo.write('digraph G\n{\n\tnode [shape=circle, fontsize='+str(font_size_label)+'];\n\tlayout="'+layout+'";\n\tsize="10,10"\n')
        archivo.write(coordenadas)
        for a in G.A:
            if str(a.vf.info) != "":
                if p:                    
                    if pos_arista(G.A, Arista(a.vf, a.vi, a.weight)) != -1:
                        if camino:
                            if pos_aris_en_aris(Arista(a.vi, a.vf, a.weight),LC) != -1:
                                archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '[fontcolor=blue label='+str(a.weight)+',fontcolor="red",fontsize="'+str(font_size_label)+'", color="red", penwidth=3.0, fontname="times-bold"]\n')
                            elif pos_aris_en_aris(Arista(a.vf, a.vi, a.weight),LC) != -1:
                                archivo.write('\t'+str(a.vf.info) + ' -> ' + str(a.vi.info) + '[fontcolor=blue label='+str(a.weight)+',fontcolor="red",fontsize="'+str(font_size_label)+'", color="red", penwidth=3.0, fontname="times-bold"]\n')
                            else:                                                                            
                                archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '[fontcolor=blue label='+str(a.weight)+', dir="both", fontsize="'+str(font_size_label)+'", fontname="times-bold"]\n')
                        else:                                                                            
                            archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '[fontcolor=blue label='+str(a.weight)+', dir="both", fontsize="'+str(font_size_label)+'", fontname="times-bold"]\n')
                        #if pos_aris_en_aris(Arista(a.vf, a.vi),G.A) != -1:
                        del G.A[pos_arista(G.A, Arista(a.vf, a.vi, a.weight))]                                          
                    else:
                        if camino:
                            if pos_aris_en_aris(Arista(a.vi, a.vf, a.weight),LC) != -1:
                                archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '[fontcolor=blue label='+str(a.weight)+',fontcolor="red",fontsize="'+str(font_size_label)+'", color="red", penwidth=3.0, fontname="times-bold"]\n')
                            else:
                                archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '[fontcolor=blue label='+str(a.weight)+', fontsize="'+str(font_size_label)+'", fontname="times-bold"]\n')
                        else:
                            archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '[fontcolor=blue label='+str(a.weight)+', fontsize="'+str(font_size_label)+'", fontname="times-bold"]\n')                         
                else:
                    archivo.write('\t'+str(a.vi.info) + ' -> ' + str(a.vf.info) + '\n')
            else:
                 archivo.write('\t'+str(a.vi.info) +'\n')
        archivo.write('\tlabel="'+nombre+'" fontsize='+str(font_size_label)+'\n}')
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
    plt.axis('off')
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
