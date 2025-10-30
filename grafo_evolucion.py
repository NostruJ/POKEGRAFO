# Archivo: grafo_evolucion.py

from api_requests import obtener_datos_cadena

class NodoPokemon:
    # Representa un Pokémon (Nodo) en el grafo de evolución.
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.hijos = [] 

    def agregar_hijo(self, nodo_hijo):
        # Añade un nodo Pokémon como una evolución directa.
        self.hijos.append(nodo_hijo)

class GrafoEvolucion:
    # Construye y gestiona el grafo de evolución a partir de la PokeAPI.
    def __init__(self, nombre_especie: str):
        self.nombre_especie = nombre_especie.lower()
        self.raiz = None
        self.pokemons_ordenados = [] 

    def construir_grafo(self):
        # Orquesta la obtención de datos, construcción recursiva y recolección de todos los Pokémon.
        datos_cadena = obtener_datos_cadena(self.nombre_especie)
        
        if datos_cadena is None:
            return

        try:
            self.raiz = self._construir_cadena_recursivo(datos_cadena)
            self._recolectar_y_ordenar_pokemons()
            
            print(f"✅ Grafo de evolución de '{self.nombre_especie.capitalize()}' creado correctamente.")
            print(f"   Total de Pokémon en la cadena: {len(self.pokemons_ordenados)}")
            
        except Exception as e:
            print(f"❌ Error interno al construir el grafo para '{self.nombre_especie}': {e}")


    def _construir_cadena_recursivo(self, datos_cadena: dict):
        # Crea nodos de forma recursiva a partir de la estructura JSON jerárquica de la cadena.
        nombre_actual = datos_cadena["species"]["name"]
        nodo_actual = NodoPokemon(nombre_actual)

        for evoluciona_a in datos_cadena["evolves_to"]:
            nodo_hijo = self._construir_cadena_recursivo(evoluciona_a)
            nodo_actual.agregar_hijo(nodo_hijo) 

        return nodo_actual

    def _recolectar_y_ordenar_pokemons(self):
        # Recorre el grafo para obtener todos los nombres de Pokémon y los ordena.
        lista_pokemons = []
        self._recolectar_pokemons_recursivo(self.raiz, lista_pokemons)
        self.pokemons_ordenados = sorted(lista_pokemons)

    def _recolectar_pokemons_recursivo(self, nodo: NodoPokemon, lista_pokemons: list):
        # Realiza un recorrido (DFS) del grafo guardando los nombres de cada nodo.
        if nodo:
            lista_pokemons.append(nodo.nombre)
            for hijo in nodo.hijos:
                self._recolectar_pokemons_recursivo(hijo, lista_pokemons)
    
    def obtener_pokemons_ordenados(self) -> list:
        # Retorna la lista ordenada de Pokémon para usar con la Búsqueda Binaria.
        return self.pokemons_ordenados