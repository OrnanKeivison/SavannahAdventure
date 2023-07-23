#criação da superclasse aniamal 
class Animal:
    #iniciando o construtor com os respectivos atributos
    def __init__(self, name, color, gender, speed, Weight, posX, posY):
        self.__name = name
        self.__color = color
        self.__gender = gender
        self.__speed = int(speed)
        self.__Weight = int(Weight)
        self.__posX = int(posX)
        self.__posY = int(posY)

        #atributo predefinido
        self.__stamina = 100

    #métodos get's 
    def getName(self):
        return self.__name

    def getColor(self):
        return self.__color

    def getGender(self):
        return self.__gender

    def getSpeed(self):
        return self.__speed
    
    def getWeight(self):
        return self.__Weight

    def getStamina(self):
        return self.__stamina
    
    def getPosX(self):
        return self.__posX

    def getPosY(self):
        return self.__posY

    #métodos set's
    def setName(self, name):
        self.__name = name

    def setColor(self, color):
        self.__color = color

    def setGender(self, gender):
        self.__gender = gender

    def setSpeed(self, speed):
        self.__speed = int(speed)
    
    def setWeight(self, Weight):
        self.__Weight = int(Weight)

    def setStamina(self, stamina):
        self.__stamina = int(stamina)
    
    def setPosX(self, posX):
        self.__posX = int(posX)

    def setPosY(self, posY):
        self.__posY = int(posY)

    #método de impressão das características básicas do animal
    def print_attributes(self):
        print('CARACTERÍSTICAS:')
        print('nome:',self.__name)
        print('cor:',self.__color)
        print('sexo:',self.__gender)
        print('velocidade:',self.__speed)
        print('peso:',self.__Weight)
        print('estamina:',self.__stamina)
        print('posição x:',self.__posX)
        print('posição y:',self.__posY)

    #iniciando o método de emitir som com polimorfizmo
    def make_sound(self):
        pass

#criação da classe savannah
class Savannah:
    pass