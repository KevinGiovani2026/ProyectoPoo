from pokemonClase import Pokemon


class Planta(Pokemon):

        def __init__(self, nombre, hp_actual, hp_maximo, energia_actual,energia_maxima):
                super().__init__(nombre, hp_actual, hp_maximo, energia_actual,energia_maxima)


        def ataque(self,oponente):
                from pokemon_clase_agua import Agua 
                if isinstance(oponente, Agua):
                       damage = 20
                       
                else:
                        damage = 10
                        
                oponente.hp_actual -= damage
         