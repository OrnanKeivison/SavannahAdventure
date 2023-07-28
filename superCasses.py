#criação da superclasse aniamal 
class Animal:
    #iniciando o construtor com os respectivos atributos
    def __init__(self, name, color, gender, speed, Weight, posX, posY):
        self.name = name
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
        return self.name

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
        self.name = name

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
        print('nome:',self.name)
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

#classe onde ocorrem as interações dos objetos com o tabuleiro
class Savannah:
    #iniciando o construtor com o atributo
    def __init__(self, animais):
        self.__animais = animais

        #posições validas da savannah
        self.__pos11 = (1,0)
        self.__pos12 = (100,0)
        self.__pos13 = (200,0)
        self.__pos14 = (300,0)
        self.__pos15 = (400,0)
        self.__pos16 = (500,0)

        self.__pos21 = (1,100)
        self.__pos22 = (100,100)
        self.__pos23 = (200,100)
        self.__pos24 = (300,100)
        self.__pos25 = (400,100)
        self.__pos26 = (500,100)

        self.__pos31 = (1,200)
        self.__pos32 = (100,200)
        self.__pos33 = (200,200)
        self.__pos34 = (300,200)
        self.__pos35 = (400,200)
        self.__pos36 = (500,200)

        self.__pos41 = (1,300)
        self.__pos42 = (100,300)
        self.__pos43 = (200,300)
        self.__pos44 = (300,300)
        self.__pos45 = (400,300)
        self.__pos46 = (500,300)

        self.__pos51 = (1,400)
        self.__pos52 = (100,400)
        self.__pos53 = (200,400)
        self.__pos54 = (300,400)
        self.__pos55 = (400,400)
        self.__pos56 = (500,400)

        self.__pos61 = (1,500)
        self.__pos62 = (100,500)
        self.__pos63 = (200,500)
        self.__pos64 = (300,500)
        self.__pos65 = (400,500)
        self.__pos66 = (500,500)
        
        self.__posicoes = [[self.__pos11, self.__pos12, self.__pos13, self.__pos14, self.__pos15, self.__pos16],
                           [self.__pos21, self.__pos22, self.__pos23, self.__pos24, self.__pos25, self.__pos26],
                           [self.__pos31, self.__pos32, self.__pos33, self.__pos34, self.__pos35, self.__pos36],
                           [self.__pos41, self.__pos42, self.__pos43, self.__pos44, self.__pos45, self.__pos46],
                           [self.__pos51, self.__pos52, self.__pos53, self.__pos54, self.__pos55, self.__pos56],
                           [self.__pos61, self.__pos62, self.__pos63, self.__pos64, self.__pos65, self.__pos66]]

    #método get
    def getAnimais(self):
        return self.__animais

    #método andar
    def andar(self, animal, pos):
        if pos == (1, 1):
            animal.setPosX(self.__pos11[0])
            animal.setPosY(self.__pos11[1])

        elif pos == (1, 2):
            animal.setPosX(self.__pos12[0])
            animal.setPosY(self.__pos12[1])

        elif pos == (1, 3):
            animal.setPosX(self.__pos13[0])
            animal.setPosY(self.__pos13[1])

        elif pos == (1, 4):
            animal.setPosX(self.__pos14[0])
            animal.setPosY(self.__pos14[1])

        elif pos == (1, 5):
            animal.setPosX(self.__pos15[0])
            animal.setPosY(self.__pos15[1])

        elif pos == (1, 6):
            animal.setPosX(self.__pos16[0])
            animal.setPosY(self.__pos16[1])


        elif pos == (2, 1):
            animal.setPosX(self.__pos21[0])
            animal.setPosY(self.__pos21[1])

        elif pos == (2, 2):
            animal.setPosX(self.__pos22[0])
            animal.setPosY(self.__pos22[1])

        elif pos == (2, 3):
            animal.setPosX(self.__pos23[0])
            animal.setPosY(self.__pos23[1])

        elif pos == (2, 4):
            animal.setPosX(self.__pos24[0])
            animal.setPosY(self.__pos24[1])

        elif pos == (2, 5):
            animal.setPosX(self.__pos25[0])
            animal.setPosY(self.__pos25[1])

        elif pos == (2, 6):
            animal.setPosX(self.__pos26[0])
            animal.setPosY(self.__pos26[1])


        elif pos == (3, 1):
            animal.setPosX(self.__pos31[0])
            animal.setPosY(self.__pos31[1])

        elif pos == (3, 2):
            animal.setPosX(self.__pos32[0])
            animal.setPosY(self.__pos32[1])

        elif pos == (3, 3):
            animal.setPosX(self.__pos33[0])
            animal.setPosY(self.__pos33[1])

        elif pos == (3, 4):
            animal.setPosX(self.__pos34[0])
            animal.setPosY(self.__pos34[1])
        
        elif pos == (3, 5):
            animal.setPosX(self.__pos35[0])
            animal.setPosY(self.__pos35[1])

        elif pos == (3, 6):
            animal.setPosX(self.__pos36[0])
            animal.setPosY(self.__pos36[1])

        
        elif pos == (4, 1):
            animal.setPosX(self.__pos41[0])
            animal.setPosY(self.__pos41[1])

        elif pos == (4, 2):
            animal.setPosX(self.__pos42[0])
            animal.setPosY(self.__pos42[1])

        elif pos == (4, 3):
            animal.setPosX(self.__pos43[0])
            animal.setPosY(self.__pos43[1])

        elif pos == (4, 4):
            animal.setPosX(self.__pos44[0])
            animal.setPosY(self.__pos44[1])

        elif pos == (4, 5):
            animal.setPosX(self.__pos45[0])
            animal.setPosY(self.__pos45[1])
        
        elif pos == (4, 6):
            animal.setPosX(self.__pos46[0])
            animal.setPosY(self.__pos46[1])


        elif pos == (5, 1):
            animal.setPosX(self.__pos51[0])
            animal.setPosY(self.__pos51[1])

        elif pos == (5, 2):
            animal.setPosX(self.__pos52[0])
            animal.setPosY(self.__pos52[1])

        elif pos == (5, 3):
            animal.setPosX(self.__pos53[0])
            animal.setPosY(self.__pos53[1])

        elif pos == (5, 4):
            animal.setPosX(self.__pos54[0])
            animal.setPosY(self.__pos54[1])
        
        elif pos == (5, 5):
            animal.setPosX(self.__pos55[0])
            animal.setPosY(self.__pos55[1])

        elif pos == (5, 6):
            animal.setPosX(self.__pos56[0])
            animal.setPosY(self.__pos56[1])
        

        elif pos == (6, 1):
            animal.setPosX(self.__pos61[0])
            animal.setPosY(self.__pos61[1])

        elif pos == (6, 2):
            animal.setPosX(self.__pos62[0])
            animal.setPosY(self.__pos62[1])

        elif pos == (6, 3):
            animal.setPosX(self.__pos63[0])
            animal.setPosY(self.__pos63[1])

        elif pos == (6, 4):
            animal.setPosX(self.__pos64[0])
            animal.setPosY(self.__pos64[1])

        elif pos == (6, 5):
            animal.setPosX(self.__pos65[0])
            animal.setPosY(self.__pos65[1])

        elif pos == (6, 6):
            animal.setPosX(self.__pos66[0])
            animal.setPosY(self.__pos66[1])

    def checar_colisao(self):
        posicoes = {} #crinado dicionário para armazenar posições
        for animal in self.__animais: 
            posicao = (animal.getPosX(), animal.getPosY())  #obtém a posição do animal
            if posicao in posicoes:
                posicoes[posicao].append(animal) #adiciona o nome do animal na sua respectiva posição
            else:
                posicoes[posicao] = [animal] #cria a novva posição e adiciona o nome do animal
        
        #adiciona colisões, se ouver, a lista colisões
        colisoes = []
        for posicao, animais in posicoes.items():
            if len(animais) > 1:
                colisoes.append((posicao, animais))
        
        return colisoes # retorna as colisões