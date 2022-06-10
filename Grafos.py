#programa para clase que implemente grafos

import numpy as np


class Grafo:
    #constructor
    def __init__(self, vertices):
        self.vertices = vertices
        self.matadyacencia = np.zeros([vertices, vertices], dtype=int)
        self.matcostos = np.zeros([vertices, vertices], dtype=float)
        self.contarcos = 0
        
    def arco(self, nodo_i, nodo_f, costo):
        self.matadyacencia[nodo_i-1, nodo_f-1] = 1
        self.matcostos[nodo_i-1, nodo_f-1] = costo
        self.contarcos = self.contarcos + 1
    
    def adyacencia(self):
        print (self.matadyacencia)
        
    def listaAdyacencia(self):
        contador = 0
        listAd = np.zeros([self.contarcos,2], dtype=int)
        for i in range (self.vertices):
            for j in range (self.vertices):
                if(self.matadyacencia[i,j]!=0):
                    listAd[contador, 0] = i+1
                    listAd[contador, 1] = j+1
                    contador = contador +1
        print(listAd)
    
    def costos(self):
        print(self.matcostos)

    def hamilton(self, inicio):
        disttotal = 0
        dist = 0
        nextnode = inicio-1
        actualnode = inicio-1
        fin = 0
        cadena = ""
        while fin < self.vertices:
            for i in range (self.vertices):
                if(self.matcostos[actualnode, i] != 0):
                    if(dist == 0):
                        dist = self.matcostos[actualnode, i]
                        nextnode = i
                    else:
                        if(self.matcostos[actualnode, i]<dist):
                            dist = self.matcostos[actualnode, i]
                            nextnode = i
            cadena = cadena + "pasa por grafo: " + str(actualnode + 1)  + " costo: " + str(dist)
            disttotal = dist + disttotal
            actualnode = nextnode
            fin = fin + 1
        print(disttotal)
        print(cadena)
        
    def dijkstra(self, nodo_i, nodo_f):
        disttotal = 0
        dist = 0
        nextnode = nodo_i-1
        actualnode = nodo_i-1
        fin = 0
        cadena = ""
        while fin < self.vertices:
            for i in range (self.vertices):
                if(self.matcostos[actualnode, i] != 0):
                    if(dist == 0):
                        dist = self.matcostos[actualnode, i]
                        nextnode = i
                    else:
                        if(self.matcostos[actualnode, i]<dist):
                            dist = self.matcostos[actualnode, i]
                            nextnode = i
            cadena = cadena + "pasa por grafo: " + str(actualnode + 1)  + " costo: " + str(dist)
            if(nextnode == nodo_f - 1):
                fin = self.vertices -2
            
            disttotal = dist + disttotal
            actualnode = nextnode
            fin = fin + 1
        print(disttotal)
        print(cadena)
            

