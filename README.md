POKEMON EVOLUTION SEARCH SYSTEM - DOCUMENTACIÓN Y GUÍA RÁPIDA

======================================================================
🇪🇸 SECCIÓN EN ESPAÑOL
======================================================================

🎯 OBJETIVO Y ARQUITECTURA
======================================================================

El proyecto desarrolla un sistema para construir y analizar **grafos de evolución** de Pokémon, consumiendo la PokeAPI e implementando algoritmos de búsqueda eficientes.

ESTRUCTURA DE ARCHIVOS:
├── pokelib.py      # Lógica, consumo de API, Grafos y Algoritmos
├── main.py         # Interfaz de usuario y Flujo principal
└── DESARROLLO.md   # Documentación completa (este archivo)

======================================================================
📋 REQUISITOS CUMPLIDOS Y CONCEPTOS CLAVE
======================================================================

1.  GRAFOS DIRIGIDOS:
    * Representación: **Lista de Adyacencia** (diccionario de Python).
    * Función: build_directed_graph() (Recursiva).

2.  RECURSIVIDAD:
    * Aplicación: Recorrido del JSON jerárquico de la cadena de evolución (evolves_to).
    * Caso Base: El Pokémon no tiene más evoluciones.

3.  BÚSQUEDA BINARIA:
    * Algoritmo: binary_search(), implementación **iterativa** con punteros.
    * Eficiencia: **O(log n)**, garantizando búsquedas rápidas en listas ordenadas.
    * Requisito: La lista de nodos debe estar **ordenada alfabéticamente** (extract_sorted_nodes()).

4.  APIS RESTful:
    * Consumo: Librería requests.
    * Endpoints clave: /pokemon-species/ y /evolution-chain/.

======================================================================
🔧 RESUMEN DE FUNCIONES EN POKELIB.PY
======================================================================

| FUNCIÓN | PROPÓSITO | COMPLEJIDAD TEMPORAL |
| :--- | :--- | :--- |
| get_evolution_chain(name) | Realiza 3 peticiones HTTP para obtener el JSON de la cadena. | O(1) |
| build_directed_graph(chain) | Construye recursivamente el diccionario de adyacencia. | O(n) |
| extract_sorted_nodes(graph) | Extrae nodos y los ordena para la búsqueda binaria. | O(n log n) |
| binary_search(list, target) | Busca un Pokémon en la lista ordenada. | O(log n) |
| display_graph(graph) | Muestra el grafo en formato legible. | O(n + e) |

======================================================================
💻 INSTRUCCIONES DE INSTALACIÓN Y USO
======================================================================

REQUISITOS:
* Python 3.7 o superior
* Librería requests

INSTALACIÓN:
pip install requests

USO:
1.  Descargue pokelib.py y main.py.
2.  Ejecute el programa desde la terminal:
    python main.py

======================================================================

***

======================================================================
🇺🇸 ENGLISH SECTION
======================================================================

🎯 OBJECTIVE AND ARCHITECTURE
======================================================================

The project develops a system to build and analyze **Pokémon evolution graphs**, consuming the PokeAPI and implementing efficient search algorithms.

FILE STRUCTURE:
├── pokelib.py      # Logic, API consumption, Graphs, and Algorithms
├── main.py         # User interface and Main program flow
└── DESARROLLO.md   # Complete documentation (this file)

======================================================================
📋 FULFILLED REQUIREMENTS AND KEY CONCEPTS
======================================================================

1.  DIRECTED GRAPHS:
    * Representation: **Adjacency List** (Python dictionary).
    * Function: build_directed_graph() (Recursive).

2.  RECURSION:
    * Application: Traversing the hierarchical JSON structure of the evolution chain (evolves_to).
    * Base Case: The Pokémon has no further evolutions.

3.  BINARY SEARCH:
    * Algorithm: binary_search(), **iterative** implementation with pointers.
    * Efficiency: **O(log n)**, guaranteeing fast searches in sorted lists.
    * Requirement: The node list must be **alphabetically sorted** (extract_sorted_nodes()).

4.  RESTful APIs:
    * Consumption: requests library.
    * Key Endpoints: /pokemon-species/ and /evolution-chain/.

======================================================================
🔧 POKELIB.PY FUNCTION SUMMARY
======================================================================

| FUNCTION | PURPOSE | TEMPORAL COMPLEXITY |
| :--- | :--- | :--- |
| get_evolution_chain(name) | Performs 3 HTTP requests to get the chain JSON. | O(1) |
| build_directed_graph(chain) | Recursively builds the adjacency dictionary. | O(n) |
| extract_sorted_nodes(graph) | Extracts and sorts nodes for binary search. | O(n log n) |
| binary_search(list, target) | Searches for a Pokémon in the sorted list. | O(log n) |
| display_graph(graph) | Shows the graph in readable format. | O(n + e) |

======================================================================
💻 INSTALLATION AND USAGE INSTRUCTIONS
======================================================================

REQUIREMENTS:
* Python 3.7 or higher
* requests library

INSTALLATION:
pip install requests

USAGE:
1.  Download pokelib.py and main.py.
2.  Execute the program from the terminal:
    python main.py
======================================================================