# Archivo: busqueda_optimizada.py

def busqueda_binaria(lista_ordenada: list, objetivo: str) -> bool:
    # Implementa el algoritmo iterativo de Búsqueda Binaria con complejidad O(log n).
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        valor_medio = lista_ordenada[medio]

        if valor_medio == objetivo:
            return True 
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
            
    return False