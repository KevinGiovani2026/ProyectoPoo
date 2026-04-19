from pokemonClase import Pokemon
from pokemon_clase_fuego import Fuego

class Agua(Pokemon):

        def __init__(self, nombre, hp_actual, hp_maximo, energia_actual,energia_maxima):
                super().__init__(nombre, hp_actual, hp_maximo, energia_actual,energia_maxima)

        def ataque(self, oponente):
                validar_objeto = oponente
                if isinstance(oponente, Fuego):
                        damage = 20 
                        oponente.hp_actual -= damage
                        
                else:
                        oponente.hp_actual -= 10