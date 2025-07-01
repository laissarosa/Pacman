import pygame
import math
import os
import sys
from pygame import Surface

pygame.init()

class Labirinto:
    def __init__(self) -> None:
        self.__inicializar()
        self.__tabuleiro = [[6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
        [3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
        [3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
        [3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
        [3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
        [3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],         
        [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
        [8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 9, 9, 9, 9, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
        [4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
        [5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
        [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
        [3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
        [3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
        [3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
        [3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
        [3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3], #corrigir depois
        [3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
        [7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
                ]
        self.__piscar = False
        self.__contador = 0
        self.__todas_bolinhas = 246

    @property
    def piscar(self):
        return self.__piscar

    @piscar.setter
    def piscar(self, value):
        self.__piscar = value

    @property
    def contador(self):
        return self.__contador

    @contador.setter
    def contador(self, value):
        self.__contador = value

    @property
    def todas_bolinhas(self):
        return self.__todas_bolinhas

    @todas_bolinhas.setter
    def todas_bolinhas(self, value):
        self.__todas_bolinhas = value

    @property
    def tabuleiro(self):
        return self.__tabuleiro

    @tabuleiro.setter
    def tabuleiro(self, tabuleiro):
        self.__tabuleiro = tabuleiro 

    def __inicializar(self) -> None:
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    def desenhar_tabuleiro (self, tela: Surface, celula_largura: int, celula_altura: int) -> None:
        PI = math.pi 
        ajuste_alt  = celula_altura
        ajuste_lag = celula_largura 
        for i in range (len(self.tabuleiro)):
            for j in range (len(self.tabuleiro[i])):
                if self.tabuleiro[i][j] == 1:
                        pygame.draw.circle(tela, 'white' , (j * ajuste_lag + (0.5 * ajuste_lag), i * ajuste_alt + (0.5 * ajuste_alt)), 4)
                if self.tabuleiro[i][j] == 2 and self.piscar_bolinha():
                        pygame.draw.circle(tela, 'white' , (j *ajuste_lag + (0.5 * ajuste_lag), i * ajuste_alt + (0.5 * ajuste_alt)), 7)
                if self.tabuleiro[i][j] == 3:
                    pygame.draw.line(tela, 'blue' , (j * ajuste_lag + (0.5 * ajuste_lag), i * ajuste_alt), (j * ajuste_lag + (0.5 * ajuste_lag), i * ajuste_alt + ajuste_alt), 3)
                if self.tabuleiro[i][j] == 4:
                    pygame.draw.line(tela, 'blue' , (j * ajuste_lag , i * ajuste_alt + (0.5 * ajuste_alt)), (j * ajuste_lag + ajuste_lag, i * ajuste_alt + (0.5 * ajuste_alt)), 3)
                if self.tabuleiro[i][j] == 5:
                    pygame.draw.arc(tela, 'blue', [(j * ajuste_lag - (ajuste_lag * 0.5)), (i * ajuste_alt + (0.5 * ajuste_alt)), ajuste_lag, ajuste_alt], 0 , PI/2, 3)
                if self.tabuleiro[i][j] == 6:
                    pygame.draw.arc(tela, 'blue', [(j * ajuste_lag + (ajuste_lag * 0.5)), (i * ajuste_alt + (0.5 * ajuste_alt)), ajuste_lag, ajuste_alt], PI/2, PI, 3)
                if self.tabuleiro[i][j] == 7:
                    pygame.draw.arc(tela, 'blue', [(j * ajuste_lag + (ajuste_lag * 0.5)), (i * ajuste_alt - (0.5 * ajuste_alt)), ajuste_lag, ajuste_alt], PI, 3*PI/2, 3)
                if self.tabuleiro[i][j] == 8:
                    pygame.draw.arc(tela, 'blue', [(j * ajuste_lag - (ajuste_lag * 0.5)), (i * ajuste_alt - (0.5 * ajuste_alt)), ajuste_lag, ajuste_alt], 3*PI/2, 2*PI, 3)
                if self.tabuleiro[i][j] == 9:
                    pygame.draw.line(tela, 'white', (j * ajuste_lag, i * ajuste_alt + (0.5 * ajuste_alt)), (j * ajuste_lag + ajuste_lag, i * ajuste_alt + (0.5 * ajuste_alt)), 3)   

    def piscar_bolinha(self) -> bool:
        self.contador += 1
        if self.contador >= 60:
            self.contador = 0
            self.piscar = not self.piscar 
        return self.piscar

