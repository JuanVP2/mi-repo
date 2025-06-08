import re


class Personaje:
    def __init__(self, nombre, vida, fuerza, inteligencia, ataque):
        self.__nombre = nombre
        self.__vida = vida
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__ataque = ataque

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_vida(self):
        return self.__vida

    def get_fuerza(self):
        return self.__fuerza

    def get_inteligencia(self):
        return self.__inteligencia

    def get_ataque(self):
        return self.__ataque

    # Setters (si deseas permitir modificar desde fuera)
    def set_vida(self, nueva_vida):
        self.__vida = nueva_vida

    def set_fuerza(self, nueva_fuerza):
        if nueva_fuerza < 0:
            print("Fuerza incorrecta")
        else:
            
            self.__fuerza = nueva_fuerza

    def set_ataque(self, nuevo_ataque):
        self.__ataque = nuevo_ataque

    # Métodos
    def atributos(self):
        print(self.__nombre + ":")
        print("Fuerza:", self.__fuerza)
        print("Inteligencia:", self.__inteligencia)
        print("Vida:", self.__vida)
        print("Ataque:", self.__ataque)

    def subir_nivel(self, vida, fuerza, ataque):
        self.__vida += vida
        self.__fuerza += fuerza
        self.__ataque += ataque

    def esta_vivo(self):
        return self.__vida > 0

    def esta_muerto(self):
        self.__vida = 0
        print(self.__nombre, "está muerto")

    def dano(self, mi_enemigo):
        dano_causado = self.__ataque
        nueva_vida = mi_enemigo.get_vida() - dano_causado
        mi_enemigo.set_vida(max(nueva_vida, 0))
        return dano_causado

    def atacar(self, mi_enemigo):
        pegar = self.dano(mi_enemigo)
        print(self.__nombre, "ha realizado:", pegar, "puntos de daño")
        if mi_enemigo.esta_vivo():
            print("La vida de", mi_enemigo.get_nombre(), "es", mi_enemigo.get_vida())
        else:
            mi_enemigo.esta_muerto()



class Guerrero(Personaje):
    #modificar el constructor para una nueva variable
    def __init__(self, nombre, vida, fuerza, inteligencia, ataque, ki):
        #nos permite acceder a los atributos y metodos de la super clase
        #no hace falta self viene implisito en el super
        super().__init__(nombre, vida, fuerza, inteligencia, ataque)
        self.ki = ki
    
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10: "))
        if opcion == 1:
            self.ki = 8
        elif opcion == 2:
            self.ki = 10
        else:
            print("Numero incorrecto")

    def atributos(self):
        #modificar el metodo con supero para agregar ki
        super().atributos()
        print("ki: ", self.ki)
    
    def dano(self, mi_enemigo):
        return self.dano * self.ki - mi_enemigo.vida

class Mago(Personaje):

    def __init__(self, nombre, vida, fuerza, inteligencia, ataque, libro):
        super().__init__(nombre, vida, fuerza, inteligencia, ataque)
        #le escribimos el argumento 
        self.libro = libro

    def atributos(self):
        super().atributos()
        return print("Libro", self.libro)
    
    def dano(self, mi_enemigo):
        return self.__inteligencia * self.libro - mi_enemigo.vida

goku = Guerrero("goku", 500, 300, 100, 100,2)
goku.atributos()
#goku.cambiar_arma()
goku.atributos()
#constructor guardado en una variable asi se crea un objeto personaje
mi_personaje = Personaje("boss", 5000, 400, 1000, 10000)
mi_enemigo = Personaje("bulba", 10000, 100, 500, 2000)
#print("Nombre del personaje: ", mi_personaje.nombre)
#print("Inteligencia: ", mi_personaje.inteligencia)
#mi_personaje.atributos()
#mi_personaje.subir_nivel(5500, 450, 50)
#mi_personaje.atributos()
#print(mi_personaje.esta_vivo())
#mi_personaje.esta_muerto()
#mi_personaje.atributos()
#print(mi_personaje.dano(mi_enemigo))
#mi_personaje.atacar(mi_enemigo)
#print(mi_personaje.__fuerza)

##ENCAPSULAMIETO
#print(mi_personaje.set_fuerza(0))


#mi_personaje = Personaje("tortuga", 300, 40, 10, 80)
#mi_personaje.atributos()