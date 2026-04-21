
from pokemonClase import Pokemon



class Agua(Pokemon):

        def __init__(self, nombre, hp_actual, hp_maximo, energia_actual,energia_maxima):
                super().__init__(nombre, hp_actual, hp_maximo, energia_actual,energia_maxima)


        def ataque(self, oponente):
                from pokemon_clase_fuego import Fuego 
                if isinstance(oponente, Fuego):
                        damage = 20
                else:
                        damage = 10
                
                oponente.hp_actual -= damage


