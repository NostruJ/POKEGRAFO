# Archivo: grafo_evolucion.py

from api_requests import obtener_datos_cadena

class NodoPokemon:
    """Representa un Pokémon (Nodo) en el grafo de evolución."""
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.hijos = [] 

    def agregar_hijo(self, nodo_hijo):
        """Añade un nodo Pokémon como una evolución directa."""
        self.hijos.append(nodo_hijo)

class GrafoEvolucion:
    """Construye y gestiona el grafo de evolución a partir de la PokeAPI."""
    def __init__(self, nombre_especie: str):
        self.nombre_especie = nombre_especie.lower()
        self.raiz = None
        self.pokemons_ordenados = [] 

    def construir_grafo(self):
        """Método principal que orquesta la construcción del grafo y recolecta los Pokémon."""
        # Se llama a la función de la API
        datos_cadena = obtener_datos_cadena(self.nombre_especie)
        
        if datos_cadena is None:
            # Si obtener_datos_cadena falló, el grafo no se construye
            return

        try:
            # 🔄 Llamada a la función recursiva para construir el árbol/grafo
            self.raiz = self._construir_cadena_recursivo(datos_cadena)
            
            # Recolectar y ordenar TODOS los nombres
            self._recolectar_y_ordenar_pokemons()
            
            print(f"✅ Grafo de evolución de '{self.nombre_especie.capitalize()}' creado correctamente.")
            print(f"   Total de Pokémon en la cadena: {len(self.pokemons_ordenados)}")
            
        except Exception as e:
            # Manejo de errores internos durante la construcción
            print(f"❌ Error interno al construir el grafo para '{self.nombre_especie}': {e}")


    def _construir_cadena_recursivo(self, datos_cadena: dict):
        """
        🔄 Función Recursiva: Crea nodos a partir de la estructura JSON jerárquica.
        """
        nombre_actual = datos_cadena["species"]["name"]
        nodo_actual = NodoPokemon(nombre_actual)

        for evoluciona_a in datos_cadena["evolves_to"]:
            nodo_hijo = self._construir_cadena_recursivo(evoluciona_a)
            nodo_actual.agregar_hijo(nodo_hijo) 

        return nodo_actual

    def _recolectar_y_ordenar_pokemons(self):
        """Recorre el grafo, recolecta los nombres y los ordena."""
        lista_pokemons = []
        # Llamada a la función recursiva de recorrido
        self._recolectar_pokemons_recursivo(self.raiz, lista_pokemons)
        self.pokemons_ordenados = sorted(lista_pokemons)

    def _recolectar_pokemons_recursivo(self, nodo: NodoPokemon, lista_pokemons: list):
        """Función recursiva para hacer un recorrido (DFS) y guardar los nombres."""
        if nodo:
            lista_pokemons.append(nodo.nombre)
            for hijo in nodo.hijos:
                self._recolectar_pokemons_recursivo(hijo, lista_pokemons)
    
    def obtener_pokemons_ordenados(self) -> list:
        """Retorna la lista ordenada de Pokémon para la Búsqueda Binaria."""
        return self.pokemons_ordenados