
from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible

from pokemon_clase_agua import Agua
from pokemon_clase_electrico import Electrico
from pokemon_clase_fuego import Fuego
from pokemon_clase_planta import Planta

def seleccionar_pokemon():
    print("Elige tu Pokémon:")
    print("tipo 1. Agua | tipo 2. Electrico | tipo 3. Fuego | tipo 4. Planta")
    
    seleccion = input("Ingresa el número: ")
    
    datos = CATALOGO_POKEMON[seleccion]
    
    if seleccion == "1":
        mi_pokemon = Agua(datos["nombre"], datos["hp_maximo"], datos["hp_maximo"], datos["energia_maxima"], datos["energia_maxima"]) 
    elif seleccion == "2":
        mi_pokemon = Electrico(datos["nombre"], datos["hp_maximo"], datos["hp_maximo"], datos["energia_maxima"], datos["energia_maxima"])
    elif seleccion == "3":
        mi_pokemon = Fuego(datos["nombre"], datos["hp_maximo"], datos["hp_maximo"], datos["energia_maxima"], datos["energia_maxima"])
    elif seleccion == "4":
        mi_pokemon = Planta(datos["nombre"], datos["hp_maximo"], datos["hp_maximo"], datos["energia_maxima"], datos["energia_maxima"])
    else:
        print("Opción inválida")
        return None  
        
    print(f"Has seleccionado a {mi_pokemon.nombre}!")
    return mi_pokemon



print("="*30)
print("Simulador de Batallas Pokemon")
print("="*30)

while True:
    print("Seleccione el Modo de Juego")
    print("1. Jugador vs Jugador")
    print("2. Jugador vs Computadora")

    opcion = input("SELECCIONE MODO DE JUEGO:")
    if opcion == "1":
        mostrar_catalogo_disponible()
        pokemon1 = seleccionar_pokemon()
        if pokemon1 is None:
            print("No se pudo seleccionar un Pokémon válido.")
        else:
            pokemon2 = seleccionar_pokemon()
            
        



