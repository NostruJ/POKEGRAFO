# ⚡ Poké-Grafo y Búsqueda Binaria (Pokémon Evolution Graph and Binary Search)

Este proyecto es una aplicación de consola en Python diseñada para construir el **grafo de evolución** de cualquier Pokémon base utilizando la **PokeAPI**. Una vez construida la cadena de evolución, utiliza un algoritmo de **búsqueda binaria** altamente eficiente para determinar rápidamente si un Pokémon específico forma parte de esa cadena.

El código está optimizado con **caching** y un manejo de errores robusto para garantizar un rendimiento óptimo y evitar peticiones redundantes a la API.

---

## 🇪🇸 Documentación en Español

### 📝 Descripción

La aplicación modela la cadena de evolución como un **Grafo Dirigido** (`GrafoEvolucion`), donde cada Pokémon es un **Nodo** (`NodoPokemon`).

* **Optimización:** Utiliza `@lru_cache` para guardar en memoria las cadenas de evolución ya consultadas, evitando peticiones repetidas a la PokeAPI.
* **Eficiencia:** Implementa la función `buscar_binario` basada en el módulo estándar de Python `bisect`, ofreciendo una complejidad de tiempo de **$O(\log n)$** (logarítmica) para la búsqueda.

### ⚙️ Requisitos

* Python 3.x
* Librería `requests`

Para instalar la librería `requests`:

```bash
pip install requests