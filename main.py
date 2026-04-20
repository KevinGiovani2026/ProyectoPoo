
import random

from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible

from pokemon_clase_agua import Agua
from pokemon_clase_electrico import Electrico
from pokemon_clase_fuego import Fuego
from pokemon_clase_planta import Planta

def seleccionar_pokemon(turno_computadora = None):
    if turno_computadora:
        seleccion = turno_computadora
    
    else:
        print("Elige tu Pokémon:")
        print("tipo 1. Agua | tipo 2. Electrico | tipo 3. Fuego | tipo 4. Planta")
        seleccion = input("Ingresa el número: ")
    
    if seleccion not in CATALOGO_POKEMON:
        print("Opción inválida")
        return None
    
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
        
    
    print(f"¡Has seleccionado a {mi_pokemon.nombre}!")
    return mi_pokemon

def realizar_turno(atacante, defensor, es_computadora=False):
    print(f"\nEs el turno de {atacante.nombre} (HP: {atacante.hp_actual}, Energía: {atacante.energia_actual})")
    
    if es_computadora:
        opcion = random.choice(["1", "2", "3"])
        print(f"Computadora elige: {'Atacar' if opcion == '1' else 'Defender' if opcion == '2' else 'Descansar'}")
    else:
        print("1. Atacar | 2. Defender | 3. Descansar")
        opcion = input("Elige una acción: ")
    
    if opcion == "1":
        atacante.ataque(defensor)
    elif opcion == "2":
        atacante.defensa()
    elif opcion == "3":
        atacante.descanso()

def iniciar_batalla(p1, p2, modo_vs_cpu=False):
    turno = 1
    while p1.hp_actual > 0 and p2.hp_actual > 0:
        print(f"\n--- Turno {turno} ---")
        
        # Turno Jugador 1
        realizar_turno(p1, p2, es_computadora=False)
        if p2.hp_actual <= 0:
            print(f"¡{p2.nombre} ha sido derrotado! {p1.nombre} gana.")
            break
            
        # Turno Jugador 2 o Computadora
        realizar_turno(p2, p1, es_computadora=modo_vs_cpu)
        if p1.hp_actual <= 0:
            print(f"¡{p1.nombre} ha sido derrotado! {p2.nombre} gana.")
            break
            
        turno += 1


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
        print("Turno Jugador 1")
        pokemon1 = seleccionar_pokemon()
        if pokemon1 is None:
            print("No se pudo seleccionar un Pokémon válido.")
        else:
            print("Turno Jugador 2")
            pokemon2 = seleccionar_pokemon()

            iniciar_batalla(pokemon1, pokemon2, modo_vs_cpu=False)



    elif opcion == "2":
        pokemon1 = seleccionar_pokemon() 
        if pokemon1:
            seleccion_random = random.choice(["1", "2", "3", "4"])
            pokemon2 = seleccionar_pokemon(seleccion_random) 
            print(f"La computadora ha seleccionado a {pokemon2.nombre}!")

            iniciar_batalla(pokemon1, pokemon2, modo_vs_cpu=True)
        



