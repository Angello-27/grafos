import folium
import webbrowser


def mostrar(grafo):
    zoom = 14
    santa_cruz = [-17.783118, -63.181258]
    mapa = folium.Map(location=santa_cruz, zoom_start=zoom)
    marcar(grafo, mapa)
    mapa.save('mapa.html')
    webbrowser.open('mapa.html', new=0, autoraise=True)


def marcar(grafo, mapa):
    tooltip = 'Haga clic para más información'
    for nodo in grafo:
        popup = "<strong>" + nodo.getNombre() + "</strong>"
        folium.Marker([nodo.getLatitud(), nodo.getLongitud()],
                      tooltip=tooltip,
                      popup=popup).add_to(mapa)
