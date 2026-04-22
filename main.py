
import random

from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible

from pokemon_clase_agua import Agua
from pokemon_clase_electrico import Electrico
from pokemon_clase_fuego import Fuego
from pokemon_clase_planta import Planta

def seleccionar_pokemon(turno_computadora = None, entrenador = "Jugador"):
    if turno_computadora:
        seleccion = turno_computadora
    
    else:
        print(f"{entrenador}, elige tu Pokémon:")
        mostrar_catalogo_disponible()
        seleccion = input("Ingresa el número: ")
    
    if seleccion not in CATALOGO_POKEMON:
        print("Opción inválida")
        return None
    
    datos = CATALOGO_POKEMON[seleccion]
    
    if datos["tipo"] == "Agua":
        mi_pokemon = Agua(datos["nombre"], datos["hp_maximo"], datos["hp_maximo"], datos["energia_maxima"], datos["energia_maxima"]) 
    elif datos["tipo"] == "Electrico":
        mi_pokemon = Electrico(datos["nombre"], datos["hp_maximo"], datos["hp_maximo"], datos["energia_maxima"], datos["energia_maxima"])
    elif datos["tipo"] == "Fuego":
        mi_pokemon = Fuego(datos["nombre"], datos["hp_maximo"], datos["hp_maximo"], datos["energia_maxima"], datos["energia_maxima"])
    elif datos["tipo"] == "Planta":
        mi_pokemon = Planta(datos["nombre"], datos["hp_maximo"], datos["hp_maximo"], datos["energia_maxima"], datos["energia_maxima"])
    else:
        print("Opción inválida")
        return None  
        
    
    print(f"¡{entrenador} seleccionó a {mi_pokemon.nombre}!")
    return mi_pokemon

def realizar_turno(atacante, defensor, es_computadora=False):
    print(f"\nEs el turno de {atacante.nombre} (HP: {atacante.hp_actual}, Energía: {atacante.energia_actual})")
    
    if es_computadora:
        opcion = random.choice(["1", "2", "3"])
        print(f"Computadora elige: {'Atacar' if opcion == '1' else 'Defender' if opcion == '2' else 'Descansar'}")
    else:
        while True:
            try:
                print("1. Atacar | 2. Defender | 3. Descansar")
                opcion = input("Elige una acción (1-3): ")
                
                
                if opcion not in ["1", "2", "3"]:
                    raise ValueError("Opción fuera de rango.")
                
                break 
                
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entre 1 y 3.")
    
    if opcion == "1":
        atacante.ataque(defensor)
    elif opcion == "2":
        atacante.defensa()
    elif opcion == "3":
        atacante.descanso()

def iniciar_batalla(pokemon_jugador, pokemon_rival, modo_vs_cpu=False):
    turno = 1
    while pokemon_jugador.hp_actual > 0 and pokemon_rival.hp_actual > 0:
        print(f"\n--- Round numero {turno} ---")
        
        
        realizar_turno(atacante=pokemon_jugador, defensor=pokemon_rival, es_computadora=False)
        if pokemon_rival.hp_actual <= 0:
            print(f"¡{pokemon_rival.nombre} ha sido derrotado! {pokemon_jugador.nombre} gana.")
            break
            
       
        realizar_turno(atacante=pokemon_rival, defensor=pokemon_jugador, es_computadora=modo_vs_cpu)
        if pokemon_jugador.hp_actual <= 0:
            print(f"¡{pokemon_jugador.nombre} ha sido derrotado! {pokemon_rival.nombre} gana.")
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
        while True:
            print("Turno Jugador 1")
            pokemon1 = seleccionar_pokemon()
            if pokemon1:
                break 
            print("Inténtalo de nuevo...")

        while True:
            print("Turno Jugador 2")
            pokemon2 = seleccionar_pokemon()
            if pokemon2:
                break
            print("Inténtalo de nuevo...")

        iniciar_batalla(pokemon1, pokemon2, modo_vs_cpu=False)

    elif opcion == "2":
        while True:
            pokemon1 = seleccionar_pokemon()
            if pokemon1:
                break
            print("Inténtalo de nuevo...")
        
       
        seleccion_random = random.choice(["1", "2", "3", "4", "5", "6", "7", "8"])
        pokemon2 = seleccionar_pokemon(seleccion_random, entrenador="Computadora")
        
        iniciar_batalla(pokemon1, pokemon2, modo_vs_cpu=True) 
        



