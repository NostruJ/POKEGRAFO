# Archivo: main_menu.py

# Importar las funcionalidades desde los módulos
from grafo_evolucion import GrafoEvolucion
from busqueda_optimizada import busqueda_binaria

def principal():
    """
    Función principal que ejecuta el menú interactivo para el usuario.
    """
    POKEMON_DISPONIBLES = ["bulbasaur", "charmander", "squirtle", "pidgey", "eevee", "abra"]

    print("==================================")
    print("=== ⚛️ Poké-Grafo y Optimización ===")
    print("==================================\n")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear cadena de evolución y buscar Pokémon")
        print("2. Salir")

        opcion_modo = input("\nIngrese una opción (1 o 2): ").strip()

        if opcion_modo == "2":
            print("\n👋 ¡Gracias por usar el Poké-Grafo!")
            break

        if opcion_modo == "1":
            print("\nPokémon base disponibles para consulta:")
            for i, nombre in enumerate(POKEMON_DISPONIBLES, start=1):
                print(f"  {i}. {nombre.capitalize()}")
            print("  O ingrese cualquier otro nombre de Pokémon base.")
            
            nombre_pokemon_inicial = input("\nIngrese el nombre del Pokémon base: ").strip().lower()

            # 1. Fase de Construcción del Grafo
            print(f"\n⚙️ Creando Grafo de Evolución para '{nombre_pokemon_inicial.capitalize()}'...")
            grafo = GrafoEvolucion(nombre_pokemon_inicial)
            grafo.construir_grafo() 
            
            pokemons_en_cadena = grafo.obtener_pokemons_ordenados()
            
            if not pokemons_en_cadena:
                continue
            
            print("\n📚 Cadena de evolución completa (ordenada alfabéticamente):")
            print(" → ".join(pokemons_en_cadena))
            
            # 2. Fase de Búsqueda Binaria
            print("\n--- BÚSQUEDA BINARIA (O(log n)) ---")

            # Prueba de Concepto 1: Búsqueda de un Pokémon que sí está (Se mantiene para mostrar la funcionalidad)
            if len(pokemons_en_cadena) > 0:
                objetivo_prueba_existente = pokemons_en_cadena[0]
                resultado = busqueda_binaria(pokemons_en_cadena, objetivo_prueba_existente)
                print(f"Prueba: Buscando '{objetivo_prueba_existente.capitalize()}'... {'✅ ENCONTRADO' if resultado else '❌ NO ENCONTRADO'}")
            
            # --- SE HA ELIMINADO LA PRUEBA 2 AUTOMÁTICA ---
            # Ahora, el mensaje "❌ NO ENCONTRADO" solo aparecerá cuando
            # el usuario ingrese un Pokémon inexistente en el ciclo de abajo.

            while True:
                objetivo_busqueda = input("\nIngrese el nombre de un Pokémon para **BUSCAR** en la cadena: ").strip().lower()
                
                encontrado = busqueda_binaria(pokemons_en_cadena, objetivo_busqueda)

                if encontrado:
                    print(f"✅ El Pokémon '{objetivo_busqueda.capitalize()}' SÍ está en la cadena.")
                else:
                    # Este es el mensaje que verás si buscas un Pokémon que no está (ej: 'charmander' en la cadena de Bulbasaur)
                    print(f"❌ El Pokémon '{objetivo_busqueda.capitalize()}' NO está en la cadena.")

                otra_busqueda = input("\n¿Desea buscar otro Pokémon dentro de esta cadena? (s/n): ").strip().lower()
                if otra_busqueda != "s":
                    break
        else:
            print("⚠️ Opción inválida. Por favor, seleccione 1 o 2.")
            continue

# Ejecutar el programa principal
if __name__ == "__main__":
    principal()