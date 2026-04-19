from abc import ABC, abstractmethod #segundo dia convertimos la clase pokemon en una clase abstracta, es decir, no se pueden crear objetos de esta clase, solo se pueden crear objetos de las clases que hereden de esta clase abstracta.

class Pokemon(ABC):

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
    

    @property
    def energia_actual(self):
        return self.__energia_actual
    

    @hp_actual.setter
    def hp_actual (self, hp_actual):
        if hp_actual < 0:
            self.__hp_actual = 0
        elif hp_actual > self.hp_maximo:
            self.__hp_actual = self.hp_maximo
        else:
            self.__hp_actual = hp_actual


    @energia_actual.setter
    def energia_actual (self, energia_actual):
        if energia_actual < 0:
            self.__energia_actual = 0
        elif energia_actual > self.energia_maxima:
            self.__energia_actual = self.energia_maxima
        else:
            self.__energia_actual = energia_actual

    @abstractmethod
    def ataque(self):
        pass

    def defensa(self, daño):
        pass

    def descanso(self):
        pass

    def validar_clase(self, clase): #investigar como funciona el siguiente ejemplo
        if clase in ["Agua", "Fuego", "Planta", "Electrico"]:
            return True
        else:
            return False