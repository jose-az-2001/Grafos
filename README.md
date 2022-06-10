# Grafos
Repositorio para trabajar el proyecto de Algebra lineal de implementación de grafos

Métodos:
arco(nodo_i, nodo_f, costo): con este método se establece un arco o adyacencia entre nodos indicando el vértice de origen, vértice de destino y el peso o costo de dicho arco.

adyacencia(): con este método se invoca a la matriz de adyacencia del grafo, la cual debe ser desplegada siguiendo las reglas de generación de matrices de adyacencia.

listaAdyacencia(): con este método se invoca a la lista de adyacencia del grafo, la cual debe ser desplegada siguiendo las reglas de generación de listas de adyacencia.

costos(): con este método se invoca a la matriz de costos del grafo, la cual debe ser desplegada siguiendo las reglas de generación de matrices de costo.

hamilton(inicio): con este método se indica el vértice a partir del cual se debe iniciar la búsqueda del circuito de Hamilton y desplegar la lista que indique la trayectoria a seguir y el costo de dicha trayectoria.

dijkstra(nodo_i, nodo_f): con este método se aplica el algoritmo de Dijkstra indicando el nodo de inicio y nodo de finalización, debe desplegar la matriz / vector de costos en cada iteración del algoritmo y al finalizar mostrar el vector/matriz de la trayectoria a seguir y costo final.

