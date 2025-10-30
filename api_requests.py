# Archivo: api_requests.py

import requests
from functools import lru_cache

@lru_cache(maxsize=128)
def obtener_datos_cadena(especie_base: str):
    """
    Realiza las peticiones a la PokeAPI para obtener la cadena de evolución.
    Gestiona errores de conexión/HTTP y utiliza caché.
    """
    url_especie = f"https://pokeapi.co/api/v2/pokemon-species/{especie_base.lower()}/"
    
    try:
        # 1. Obtener la URL de la cadena
        response = requests.get(url_especie)
        response.raise_for_status() 
        datos_especie = response.json()
        
        url_cadena_evolucion = datos_especie["evolution_chain"]["url"]
        
        # 2. Obtener los datos de la cadena
        response_chain = requests.get(url_cadena_evolucion)
        response_chain.raise_for_status()
        
        return response_chain.json()["chain"]

    except requests.exceptions.HTTPError as e:
        # Manejo de error 404/4xx
        print(f"❌ Error HTTP: No se encontró el Pokémon base '{especie_base}'. (Código: {e.response.status_code})")
        return None 
    except requests.exceptions.RequestException:
        # Manejo de error de conexión
        print("❌ Error de Conexión: No se pudo conectar a la PokeAPI. Verifique su red.")
        return None
    except KeyError:
        # Manejo de error si la estructura del JSON cambia
        print("❌ Error de Datos: La estructura de la respuesta de la API no es la esperada.")
        return None