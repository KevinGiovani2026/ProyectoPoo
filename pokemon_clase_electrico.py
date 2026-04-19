from pokemonClase import Pokemon
class Electrico(Pokemon):

        def __init__(self, nombre, hp_actual, hp_maximo, energia_actual,energia_maxima):
                super().__init__(nombre, hp_actual, hp_maximo, energia_actual,energia_maxima)

        def __init__(self):
                pass

        def ataque(self, oponente):
                damage = 10
                oponente.hp_actual -= damage

