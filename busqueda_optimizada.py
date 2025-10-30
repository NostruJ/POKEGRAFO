# Archivo: busqueda_optimizada.py

def busqueda_binaria(lista_ordenada: list, objetivo: str) -> bool:
    """
    Implementación del algoritmo clásico de Búsqueda Binaria (O(log n)).
    Devuelve True si el objetivo está en la lista ordenada, False en caso contrario.
    """
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        # Calcular el índice medio
        medio = (izquierda + derecha) // 2
        
        valor_medio = lista_ordenada[medio]

        if valor_medio == objetivo:
            return True # ¡Encontrado!
        elif valor_medio < objetivo:
            # El objetivo está a la derecha
            izquierda = medio + 1
        else: # valor_medio > objetivo
            # El objetivo está a la izquierda
            derecha = medio - 1
            
    return False # No encontrado