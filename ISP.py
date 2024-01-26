from abc import ABC, abstractmethod

class Trabajador(ABC):

     @ abstractmethod
    def trabajar (self):
        pass

class Comedor(ABC):

    @ abstractmethod
    def comer (self):
        pass

   
class Durmiente(ABC):
    @ abstractmethod
    def dormir (self):
        pass


class Humano(Trabajador,Durmiente,Comedor):
    del comer(self):
    print("El humano está comiendo")

     del trabajar(self):
    print("El humano está trabajando")

     del dormir(self):
    print("El humano está durmiendo")



class Robot(Trabajador):

  del trabajar(self):
    print("El robot está trabajando")

    robot = Robot()
    humano = Humano

    robot.trabajar()
    humano.trabajar()
    humano.comer()
    humano.dormir()