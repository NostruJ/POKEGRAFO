# Archivo: api_requests.py

import requests
from functools import lru_cache

@lru_cache(maxsize=128)
def obtener_datos_cadena(especie_base: str):
    # Obtiene la cadena de evolución completa desde la PokeAPI, gestionando errores.
    url_especie = f"https://pokeapi.co/api/v2/pokemon-species/{especie_base.lower()}/"
    
    try:
        response = requests.get(url_especie)
        response.raise_for_status() 
        datos_especie = response.json()
        
        url_cadena_evolucion = datos_especie["evolution_chain"]["url"]
        
        response_chain = requests.get(url_cadena_evolucion)
        response_chain.raise_for_status()
        
        return response_chain.json()["chain"]

    except requests.exceptions.HTTPError as e:
        print(f"❌ Error HTTP: No se encontró el Pokémon base '{especie_base}'. (Código: {e.response.status_code})")
        return None 
    except requests.exceptions.RequestException:
        print("❌ Error de Conexión: No se pudo conectar a la PokeAPI. Verifique su red.")
        return None
    except KeyError:
        print("❌ Error de Datos: La estructura de la respuesta de la API no es la esperada.")
        return None