import pygame
from pygame import Surface
import random
from imagens.imagem import Imagem

class Tangerina:
    def __init__(self, imagem: Imagem):
        pygame.init()
        self.__x = 64
        self.__y = 105
        self.__ativa = True
        self.__imagem = imagem
        self.__contador = 0

    @property
    def contador(self):
        return self.__contador

    @contador.setter
    def contador(self, value):
        self.__contador = value

    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, value):
        self.__imagem = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def ativa(self):
        return self.__ativa

    @ativa.setter
    def ativa(self, value):
        self.__ativa = value

    def desenhar_tangerina(self, tela: Surface) -> None:
        if self.ativa:
            tela.blit(self.imagem.tangerina, (self.x, self.y))

    def desaparecer(self, foi_comida: bool) -> None:
        self.contador += 1
        if self.contador >= 1500:
            self.contador = 0
            self.ativa = not self.ativa
            self.x = random.choice([64, 210, 88, 193])
        if foi_comida:
            self.ativa = False