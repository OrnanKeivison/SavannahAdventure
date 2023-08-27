import pygame
from pygame.sprite import Sprite
from superCasses import Animal

#criação da suberclasse lion 
class Elephant(Animal, Sprite):
    #iniciando o construtor com os respectivos atributos
    def __init__(self, name, color, gender, speed, weight, posX, posY):
        super().__init__(name, color, gender, speed, weight, posX, posY)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/image/elephant.png') 
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = self.image.get_rect()

    #método make_sound específico para o Lion
    def make_sound(self):
        print(f'{self.name} está bramindo')
        # pygame.mixer.init()
        # roar = pygame.mixer.Sound('data/sunds/lion.wav')
        # roar.play(1)

    #método para mostrar o leão na tela
    def show_on_screen(self, screen):
        self.rect.x = self.getPosX()
        self.rect.y = self.getPosY()

        screen.blit(self.image, self.rect)

#criação da suberclasse lion 
class Giraffe(Animal, Sprite):
    #iniciando o construtor com os respectivos atributos
    def __init__(self, name, color, gender, speed, weight, posX, posY):
        super().__init__(name, color, gender, speed, weight, posX, posY)
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('data/image/giraffe.png') 
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = self.image.get_rect()

    #método make_sound específico para o Lion
    def make_sound(self):
        print(f'{self.name} está zumbindo')
        # pygame.mixer.init()
        # roar = pygame.mixer.Sound('data/sunds/lion.wav')
        # roar.play(1)

    #método para mostrar o leão na tela
    def show_on_screen(self, screen):
        self.rect.x = self.getPosX()
        self.rect.y = self.getPosY()

        screen.blit(self.image, self.rect)

#criação da suberclasse lion 
class Lion(Animal, Sprite):
    #iniciando o construtor com os respectivos atributos
    def __init__(self, name, color, gender, speed, weight, posX, posY):
        super().__init__(name, color, gender, speed, weight, posX, posY)
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('data/image/lion.png') 
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = self.image.get_rect()

    #método make_sound específico para o Lion
    def make_sound(self):
        print(f'{self.name} está rugindo')
        # pygame.mixer.init()
        # roar = pygame.mixer.Sound('data/sunds/lion.wav')
        # roar.play(1)

    #método para mostrar o leão na tela
    def show_on_screen(self, screen):
        self.rect.x = self.getPosX()
        self.rect.y = self.getPosY()

        screen.blit(self.image, self.rect)

#criação da suberclasse lion 
class Monkey(Animal, Sprite):
    #iniciando o construtor com os respectivos atributos
    def __init__(self, name, color, gender, speed, weight, posX, posY):
        super().__init__(name, color, gender, speed, weight, posX, posY)
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('data/image/monkey.png') 
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = self.image.get_rect()

    #método make_sound específico para o Lion
    def make_sound(self):
        print(f'{self.name} está guinchando')
        # pygame.mixer.init()
        # roar = pygame.mixer.Sound('data/sunds/lion.wav')
        # roar.play(1)

    #método para mostrar o leão na tela
    def show_on_screen(self, screen):
        self.rect.x = self.getPosX()
        self.rect.y = self.getPosY()

        screen.blit(self.image, self.rect)

#criação da suberclasse lion 
class Rhino(Animal, Sprite):
    #iniciando o construtor com os respectivos atributos
    def __init__(self, name, color, gender, speed, weight, posX, posY):
        super().__init__(name, color, gender, speed, weight, posX, posY)
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('data/image/rhino.png') 
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = self.image.get_rect()

    #método make_sound específico para o Lion
    def make_sound(self):
        print(f'{self.name} está grunhindo')
        # pygame.mixer.init()
        # roar = pygame.mixer.Sound('data/sunds/lion.wav')
        # roar.play(1)

    #método para mostrar o leão na tela
    def show_on_screen(self, screen):
        self.rect.x = self.getPosX()
        self.rect.y = self.getPosY()

        screen.blit(self.image, self.rect)

#criação da suberclasse lion 
class Zebra(Animal, Sprite):
    #iniciando o construtor com os respectivos atributos
    def __init__(self, name, color, gender, speed, weight, posX, posY):
        super().__init__(name, color, gender, speed, weight, posX, posY)
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('data/image/zebra.png') 
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = self.image.get_rect()

    #método make_sound específico para o Lion
    def make_sound(self):
        print(f'{self.name} está zurrando')
        # pygame.mixer.init()
        # roar = pygame.mixer.Sound('data/sunds/lion.wav')
        # roar.play(1)

    #método para mostrar o leão na tela
    def show_on_screen(self, screen):
        self.rect.x = self.getPosX()
        self.rect.y = self.getPosY()

        screen.blit(self.image, self.rect)