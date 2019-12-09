class Arista:

    def __init__(self, tiempo, distancia):
        self.tiempo = tiempo
        self.estado = False
        self.distancia = distancia

    def getTiempo(self):
        return self.tiempo

    def getDistancia(self):
        return self.distancia

    def getEstado(self):
        return self.estado

    def marcar(self):
        self.estado = True


class Vertice:

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.latitud = 0
        self.longitud = 0
        self.conectados = {}

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getConectados(self):
        return self.conectados.keys()

    def getConexion(self, item):
        return self.conectados[item]

    def conectar(self, item, conexion):
        self.conectados[item] = conexion

    def __str__(self):
        return "id:" + str(self.id) + ", nombre:" + self.nombre + \
               "\nConectados:" + str([arista for arista in self.conectados])


class Grafo:

    def __init__(self):
        self.cantidad = 0
        self.elementos = {}

    def agregar(self, nombre):
        vertice = Vertice(self.cantidad, nombre)
        self.elementos[self.cantidad] = vertice
        self.cantidad = self.cantidad + 1
        return vertice

    def obtener(self, index):
        if index in self.elementos:
            return self.elementos[index]
        else:
            return None

    def getElementos(self):
        return self.elementos.keys()

    def enlazar(self, elem1, elem2, tiempo, distancia):
        conexion = Arista(tiempo, distancia)
        self.elementos[elem1].conectar(elem2, conexion)

    def __contains__(self, item):
        return item in self.elementos

    def __iter__(self):
        return iter(self.elementos.values())
