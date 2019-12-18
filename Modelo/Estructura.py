class Arista:

    # constructor con parametros de la clase
    # atributos de la clase son el tiempo, distancia y su estado
    def __init__(self, tiempo, distancia):
        self.tiempo = tiempo
        self.estado = False
        self.distancia = distancia

    # metodo getters
    def getTiempo(self):
        return self.tiempo

    # metodo getters
    def getDistancia(self):
        return self.distancia

    # metodo getters
    def getEstado(self):
        return self.estado

    # metodo que modifica el estado de la arista
    def marcar(self, value):
        self.estado = value


class Nodo:

    # constructor con parametros de la clase
    # atributos de la clase son el id, nombre, latitud y longitud
    def __init__(self, id, nombre, latitud, longitud):
        self.id = id
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.conectados = {}  # lista de arista a los que esta conectado el nodo

    # metodo getters
    def getId(self):
        return self.id

    # metodo getters
    def getNombre(self):
        return self.nombre

    # metodo getters
    def getLatitud(self):
        return self.latitud

    # metodo getters
    def getLongitud(self):
        return self.longitud

    # metodo getters
    def getConectados(self):
        return self.conectados.keys()

    # metodo getters
    def getConexion(self, item):
        return self.conectados[item]

    # metodo encargado de conectarse con otro nodo mediante una arista
    def conectar(self, item, conexion):
        self.conectados[item] = conexion

    # metodo que imprime el id, nombre y la lista de arista de un nodo
    def __str__(self):
        return "id:" + str(self.id) + ", nombre:" + self.nombre + \
               "\nConectados:" + str([arista for arista in self.conectados])


class Grafo:

    # constructor con parametros de la clase
    # atributos de la clase son cantidad total de nodos
    def __init__(self):
        self.cantidad = 0
        self.elementos = {}  # lista de nodos dentro del grafo

    # metodo encargado de insertar un nuevo nodo al grafo
    # colocando como id del nodo el total de elementos del grafo
    def agregar(self, nombre, latitud, longitud):
        vertice = Nodo(self.cantidad, nombre, latitud, longitud)
        self.elementos[self.cantidad] = vertice
        self.cantidad = self.cantidad + 1
        return vertice

    # metodo encargado de obtener un nodo mediante su id
    def obtener(self, index):
        if index in self.elementos:
            return self.elementos[index]
        else:
            return None

    # metodo getters
    def getElementos(self):
        return self.elementos.keys()

    # metodo encargado de enlazar un nodo con otro
    # usando los id de los nodo para generar una nueva arista
    def enlazar(self, id1, id2, tiempo, distancia):
        conexion = Arista(tiempo, distancia)
        self.elementos[id1].conectar(id2, conexion)

    # metodo que permite el uso de 'in' dentro de un ciclo
    def __contains__(self, item):
        return item in self.elementos

    # metodo que permite el uso de 'in' dentro de un ciclo
    def __iter__(self):
        return iter(self.elementos.values())
