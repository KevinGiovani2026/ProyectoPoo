from pokedex import *
from pokemonClase import Pokemon
from pokemon_clase_agua import Agua
from pokemon_clase_electrico import Electrico
from pokemon_clase_fuego import Fuego
from pokemon_clase_planta import Planta

def seleccionar_pokemon():
    print("Elige tu Pokémon:")
    print("tipo 1. Agua | tipo2. Electrico | tipo 3. Fuego | tipo 4. Planta")
    
    seleccion = input("Ingresa el número: ")
    
    
    if seleccion == "1":
        mi_pokemon = Agua() 
    elif seleccion == "2":
        mi_pokemon = Electrico()
    elif seleccion == "3":
        mi_pokemon = Fuego()
    elif seleccion == "4":
        mi_pokemon = Planta()
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
        pokemon2 = seleccionar_pokemon()



