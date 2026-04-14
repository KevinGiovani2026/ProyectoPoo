class Pokemon:
    nombre = ""
    hp_actual = 100
    hp_maximo = 100
    energia_actual = 100
    energia_maxima = 100
    pass

    def __init__(self, nombre, hp_actual, hp_maximo, energia_actual,energia_maxima):
        self.nombre = nombre
        self.__hp_actual = hp_actual
        self.hp_maximo = hp_maximo
        self.__energia_actual = energia_actual
        self.energia_maxima = energia_maxima
        pass

    @property
    def hp_actual(self):
        return self.__hp_actual 
    pass

    @property
    def energia_actual(self):
        return self.__energia_actual
    pass

    @hp_actual.setter
    def hp_actual (self, hp_actual):
        pass

    @energia_actual.setter
    def energia_actual (self, energia_actual):
        pass

    def ataque():
        pass

    def defensa():
        pass

    def descanso():
        pass

class Agua(Pokemon):
        # def lanzar_hechizo(self):
        #     print("!El mago lanza una bola de fuego!") 
        pass

class Fuego(Pokemon):
        # def lanzar_hechizo(self):
        #     print("!El mago lanza una bola de fuego!") 
        pass

class Planta(Pokemon):
        # def lanzar_hechizo(self):
        #     print("!El mago lanza una bola de fuego!") 
        pass

class Electrico(Pokemon):
        pass

