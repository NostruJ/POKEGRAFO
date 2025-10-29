import requests
from functools import lru_cache
from bisect import bisect_left # Importamos la herramienta estándar para búsqueda binaria

# --- Clases de Datos (Nodos y Grafo) ---

class NodoPokemon:
    """Representa un Pokémon en el grafo de evolución."""
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

class GrafoEvolucion:
    """Construye y gestiona el grafo de evolución a partir de la PokeAPI."""
    def __init__(self, nombre_especie: str):
        self.nombre_especie = nombre_especie
        self.raiz = None

    @lru_cache(maxsize=128)
    def _obtener_datos_cadena(self, especie_base: str):
        """
        Obtiene la cadena de evolución de la PokeAPI.
        Usa lru_cache para evitar peticiones redundantes.
        """
        url_especie = f"https://pokeapi.co/api/v2/pokemon-species/{especie_base.lower()}/"
        
        # Petición a la API
        response = requests.get(url_especie)
        response.raise_for_status()  # Lanza un error si el código es 4xx o 5xx
        datos_especie = response.json()
        
        url_cadena_evolucion = datos_especie["evolution_chain"]["url"]
        
        response_chain = requests.get(url_cadena_evolucion)
        response_chain.raise_for_status()
        
        datos_cadena = response_chain.json()["chain"]
        return datos_cadena

    def construir_grafo(self):
        """Construye el grafo principal manejando errores de API."""
        try:
            # La función cacheadora espera el nombre_especie como argumento
            datos_cadena = self._obtener_datos_cadena(self.nombre_especie)
            self.raiz = self._construir_cadena_recursivo(datos_cadena)
            print("✅ Grafo de evolución creado correctamente.\n")
        
        except requests.exceptions.HTTPError as e:
            # Error común si el Pokémon no existe (ej. 404)
            print(f"❌ Error HTTP al construir el grafo: No se encontró el Pokémon base '{self.nombre_especie}'. ({e})")
        except requests.exceptions.RequestException as e:
            # Error de conexión o red
            print(f"❌ Error de conexión al construir el grafo para '{self.nombre_especie}': {e}")
        except KeyError:
            # Error si la estructura de la API cambia inesperadamente
            print(f"❌ Error de datos: La estructura de la respuesta de la API no es la esperada para '{self.nombre_especie}'.")
        except Exception as e:
            # Cualquier otro error
            print(f"❌ Error desconocido al construir el grafo para '{self.nombre_especie}': {e}")


    def _construir_cadena_recursivo(self, datos_cadena: dict):
        """Crea nodos recursivamente a partir de los datos de la API."""
        nodo = NodoPokemon(datos_cadena["species"]["name"])
        for evoluciona_a in datos_cadena["evolves_to"]:
            nodo_hijo = self._construir_cadena_recursivo(evoluciona_a)
            nodo.agregar_hijo(nodo_hijo)
        return nodo

    def obtener_todos_pokemon(self) -> list:
        """Retorna una lista ordenada con todos los nombres de Pokémon del grafo."""
        lista_pokemons = []
        self._recolectar_pokemons_recursivo(self.raiz, lista_pokemons)
        return sorted(lista_pokemons)

    def _recolectar_pokemons_recursivo(self, nodo: NodoPokemon, lista_pokemons: list):
        """Recorre el grafo (DFS) y agrega nombres a la lista."""
        if nodo:
            lista_pokemons.append(nodo.nombre)
            for hijo in nodo.hijos:
                self._recolectar_pokemons_recursivo(hijo, lista_pokemons)

# --- Función de Búsqueda Binaria Pythonica ---

def buscar_binario(lista_ordenada: list, objetivo: str) -> bool:
    """
    Realiza una búsqueda binaria eficiente usando bisect_left.
    Devuelve True si el objetivo está en la lista ordenada.
    """
    # bisect_left encuentra el índice donde se insertaría el objetivo para mantener el orden.
    indice = bisect_left(lista_ordenada, objetivo)

    # Si el índice está dentro de los límites de la lista
    # Y el elemento en ese índice es exactamente el objetivo, entonces se encuentra.
    if indice != len(lista_ordenada) and lista_ordenada[indice] == objetivo:
        return True
    return False

# --- Programa Principal ---

def principal():
    POKEMON_DISPONIBLES = [
        "bulbasaur",
        "charmander",
        "squirtle",
        "caterpie",
        "weedle",
        "pidgey",
        "ralts",
        "eevee",
        "abra",
        "machop"
    ]

    print("=== Poké-Grafo y Optimización ===\n")

    while True:
        print("\nSeleccione cómo desea buscar:")
        print("1. Escribir manualmente el nombre de un Pokémon base")
        print("2. Elegir de una lista de Pokémon disponibles")
        print("3. Salir")

        opcion_modo = input("\nIngrese una opción (1, 2 o 3): ").strip()

        if opcion_modo == "3":
            print("\n👋 ¡Gracias por usar el Poké-Grafo!")
            break

        if opcion_modo == "1":
            nombre_pokemon_inicial = input("\nIngrese el nombre del Pokémon base: ").strip().lower()

        elif opcion_modo == "2":
            print("\nPokémon base disponibles para consultar:")
            for i, nombre in enumerate(POKEMON_DISPONIBLES, start=1):
                print(f"{i}. {nombre.capitalize()}")

            seleccion_opcion = input("\nElija un Pokémon (nombre o número): ").strip().lower()

            if seleccion_opcion.isdigit() and 1 <= int(seleccion_opcion) <= len(POKEMON_DISPONIBLES):
                nombre_pokemon_inicial = POKEMON_DISPONIBLES[int(seleccion_opcion) - 1]
            elif seleccion_opcion in POKEMON_DISPONIBLES:
                nombre_pokemon_inicial = seleccion_opcion
            else:
                print("⚠️ Opción no válida. Intenta nuevamente.\n")
                continue
        else:
            print("⚠️ Opción inválida. Por favor, seleccione 1, 2 o 3.\n")
            continue

        grafo = GrafoEvolucion(nombre_pokemon_inicial)
        grafo.construir_grafo()
        
        if not grafo.raiz:
            # Si la construcción falló (ej. no existe el Pokémon), volvemos al menú.
            continue

        pokemons_en_cadena = grafo.obtener_todos_pokemon()
        print("Cadena de evolución completa:")
        print(" → ".join(pokemons_en_cadena))

        while True:
            objetivo_busqueda = input("\nIngrese el nombre de un Pokémon para buscar en la cadena: ").strip().lower()
            
            # Usamos la función optimizada de búsqueda binaria
            encontrado = buscar_binario(pokemons_en_cadena, objetivo_busqueda)

            if encontrado:
                print(f"✅ El Pokémon '{objetivo_busqueda}' SÍ está en la cadena de evolución de {nombre_pokemon_inicial}.")
            else:
                print(f"❌ El Pokémon '{objetivo_busqueda}' NO está en la cadena de evolución de {nombre_pokemon_inicial}.")

            otra_busqueda = input("\n¿Desea buscar otro Pokémon dentro de esta cadena? (s/n): ").strip().lower()
            if otra_busqueda != "s":
                break

principal()