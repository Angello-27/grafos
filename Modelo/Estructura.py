class Arista:

    # constructor de la clase
    def __init__(self, peso, linea):
        self.peso = peso
        self.linea = linea
        self.estado = False

    # metodo getters
    def getPeso(self):
        return self.peso

    # metodo getters
    def getLinea(self):
        return self.linea

    # metodo getters
    def getEstado(self):
        return self.estado

    # metodo marcar el estado de la arista
    def marcar(self, value):
        self.estado = value


class Nodo:

    # constructor de la clase
    def __init__(self, id, nombre, latitud, longitud):
        self.id = id
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.conectados = {}

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
        return self.conectados.values()

    def conectar(self, id, arista):
        self.conectados[id] = arista

    def __str__(self):
        return str(self.id) + ":" + self.nombre + " {" + str(self.latitud) + "," \
               + str(self.longitud) + "}" + "\nConectados:" + \
               str(['id:' + str(arista) + ' -> peso: ' + str(self.conectados[arista].peso)
                    for arista in self.conectados.keys()]) + "\n"


class Grafo:

    # constructor de la clase
    def __init__(self):
        self.cantidad = 0
        self.elementos = {}

    # metodo getters
    def getElementos(self):
        return self.elementos.keys()

    def agregar(self, id, nombre, latitud, longitud):
        nodo = Nodo(id, nombre, latitud, longitud)
        self.elementos[id] = nodo
        self.cantidad = self.cantidad + 1

    def existe(self, index):
        if index in self.elementos.keys():
            return True
        else:
            return False

    def obtener(self, index):
        if self.existe(index):
            return self.elementos[index]

    def enlazar(self, index1, index2, peso, linea):
        if self.existe(index1) and self.existe(index2):
            arista = Arista(peso, linea)
            nodo = self.elementos[index1]
            nodo.conectar(index2, arista)
        else:
            print("no se puede unir los elementos")

    # metodo que permite el uso de la funcion 'in' dentro del 'for'
    def __contains__(self, item):
        return item in self.elementos

    # metodo que permite el uso de la funcion 'in' dentro del 'for'
    def __iter__(self):
        return iter(self.elementos.values())
