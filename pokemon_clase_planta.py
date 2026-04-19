from pokemonClase import Pokemon


class Planta(Pokemon):

        def __init__(self, nombre, hp_actual, hp_maximo, energia_actual,energia_maxima):
                super().__init__(nombre, hp_actual, hp_maximo, energia_actual,energia_maxima)

        def __init__(self):
                pass


        def ataque(self,oponente):
                validar_objeto = oponente
                if oponente.__class__.__name__ == "Agua":
                        damage = 20 
                        oponente.hp_actual -= damage
                        
                else:
                        oponente.hp_actual -= 10
         