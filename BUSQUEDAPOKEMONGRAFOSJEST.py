import requests
import json
from typing import Dict, List, Optional

URL_EVOLUCION = "https://pokeapi.co/api/v2/evolution-chain/1/" 

def construir_grafo(nodo: Dict, grafo: Dict[str, List[str]]):
    nombre_base = nodo['species']['name']
    
    if nombre_base not in grafo:
        grafo[nombre_base] = []

    for evo in nodo.get('evolves_to', []):
        nombre_evolucionado = evo['species']['name']
        grafo[nombre_base].append(nombre_evolucionado)
        
        construir_grafo(evo, grafo)


def obtener_datos() -> Optional[Dict]:
    try:
        print(">> Conectando a la API y obteniendo la cadena de Bulbasaur...")
        respuesta = requests.get(URL_EVOLUCION)
        respuesta.raise_for_status() 
        datos = respuesta.json()
        
        grafo_evolucion: Dict[str, List[str]] = {}
        construir_grafo(datos['chain'], grafo_evolucion)
        
        nodos_ordenados = sorted(grafo_evolucion.keys())
        
        print(f">> Grafo listo. Nodos consultables: {len(nodos_ordenados)}.")

        return {
            "grafo": grafo_evolucion,
            "nodos_ordenados": nodos_ordenados
        }

    except requests.exceptions.RequestException as e:
        print(f"!! Error al obtener datos: {e}")
        return None


def buscar_pokemon(lista_ordenada: List[str], objetivo: str) -> bool:
    objetivo_lower = objetivo.lower()
    izquierda, derecha = 0, len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista_ordenada[medio] == objetivo_lower:
            return True
        elif lista_ordenada[medio] < objetivo_lower:
            izquierda = medio + 1
        else:
            derecha = medio - 1
            
    return False


def imprimir_cadena(grafo: Dict[str, List[str]]):
    print("\n--- CADENA DE EVOLUCIÓN (Bulbasaur) ---")
    
    for pokemon, evoluciones in grafo.items():
        nombre = pokemon.capitalize()
        
        if evoluciones:
            evol_str = " -> ".join(e.capitalize() for e in evoluciones)
            print(f" * {nombre} -> {evol_str}")
        else:
            print(f" * {nombre} (Final)")
    
    print("-" * 40)

def listar_consultables(nodos_ordenados: List[str]):
    print("\n--- POKÉMONES EN ESTA CADENA ---")
    print(f"Total: {len(nodos_ordenados)}")
    
    for i, poke in enumerate(nodos_ordenados, 1):
        print(f"[{i}] {poke.capitalize()}")
    print("-" * 30)


def iniciar_menu(datos: Dict):
    grafo = datos['grafo']
    nodos_ordenados = datos['nodos_ordenados']

    while True:
        print("\n=== MENÚ PRINCIPAL: POKÉ-GRAFO ===")
        print("1. Buscar Pokémon (Búsqueda Binaria)")
        print("2. Ver lista de Pokémon consultables")
        print("3. Ver la cadena de evolución (Grafo)")
        print("4. Salir")
        print("---------------------------------")
        
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == '1':
            print("\n-- BÚSQUEDA --")
            objetivo = input("Nombre del Pokémon a buscar: ").strip()
            
            if not objetivo:
                print("!! Nombre no puede estar vacío.")
                continue

            encontrado = buscar_pokemon(nodos_ordenados, objetivo)
            
            print("\n-- RESULTADO --")
            print(f"Buscado: {objetivo.capitalize()}")
            
            if encontrado:
                print("Status: ✅ ENCONTRADO.")
            else:
                print("Status: ❌ NO ENCONTRADO. (No está en la cadena de Bulbasaur)")
            print("-" * 15)

        elif opcion == '2':
            listar_consultables(nodos_ordenados)
            
        elif opcion == '3':
            imprimir_cadena(grafo)

        elif opcion == '4':
            print("\n<< Programa finalizado. >>")
            break
        
        else:
            print("!! Opción no válida. Intenta con 1, 2, 3 o 4.")


# --- Ejecución Directa ---

datos_iniciales = obtener_datos()

if datos_iniciales:
    iniciar_menu(datos_iniciales)