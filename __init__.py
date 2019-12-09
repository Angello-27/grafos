import Modelo.Estructura as modelo

g = modelo.Grafo()
for i in range(6):
    g.agregar("")

g.enlazar(0, 1, 0.5)
g.enlazar(1, 2, 0.4)
g.enlazar(2, 1, 0.2)
g.enlazar(0, 5, 0.9)
g.enlazar(1, 5, 0.3)
g.enlazar(0, 4, 0.8)
g.enlazar(5, 0, 0.1)
g.enlazar(3, 3, 0.6)
g.enlazar(0, 4, 0.7)

for v in g:
    for w in v.getConectados():
        print("( %s , %s ) --> %s" % (v.getId(), w.getId(), v.getPonderacion(w)))
