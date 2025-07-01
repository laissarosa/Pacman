import pygame

class Tela:
    def __init__(self, altura: int = 650, largura: int = 500):
        pygame.init()
        self.__altura = altura
        self.__largura = largura
        self.__tela = pygame.display.set_mode((self.largura, self.altura))
        self.__celula_largura = self.__largura // 30
        self.__celula_altura = (self.__altura - 50) // 32
        pygame.display.set_caption('PACMAN')
        
    @property
    def celula_largura(self):
        return self.__celula_largura

    @celula_largura.setter
    def celula_largura(self, celula_largura):
        self.__celula_largura = celula_largura

    @property
    def celula_altura(self):
        return self.__celula_altura

    @celula_altura.setter
    def celula_altura(self, celula_altura):
        self.__celula_altura = celula_altura

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, largura):
        self.__largura = largura

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, tela):
        self.__tela = tela


