from personagens.fantasma import Fantasma
import pygame
import random

class Inky(Fantasma):
<<<<<<< HEAD
=======

    """
    Classe que representa o fantasma Inky, caracterizado por um comportamento
    imprevisível e parcialmente aleatório.

    Inky herda a estrutura base da classe Fantasma, porém sua movimentação
    combina tentativas de avanço contínuo com mudanças de direção aleatórias
    quando encontra obstáculos, tornando seu padrão menos previsível que
    os demais fantasmas.

    Quando o Pac-Man está em estado poderoso, Inky alterna para o comportamento
    de fuga, mantendo a coerência com a mecânica principal do jogo.
    """

>>>>>>> 8639339 (add code documentation)
    def __init__(self, imagem, velocidade = 1.3):
        super().__init__(imagem, velocidade)
        pygame.init()
        self.lista_imagens = self.imagem.inky_img

    def mover(self, pacman_poderoso: bool, x_pac : int, y_pac: int, celula_largura: int, celula_altura: int, tabuleiro: list) -> None:

        if not self.fantasma_saiu:
            self.x , self.y = self.sair_da_casinha(256, 216,tabuleiro, celula_largura, celula_altura)
            if round(self.y) == 216:
                self.fantasma_saiu = True
            return 
        
        if pacman_poderoso:
            self.x , self.y, self.direcao = self.fugir(self.direcao,x_pac, y_pac, tabuleiro, celula_largura, celula_altura)
        else:
            if self.direcao == 0:
                if self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                    self.x += self.velocidade
                    return
                elif  self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                        self.direcao = 3
                        self.y += self.velocidade
                        return
                elif  self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                        self.direcao = 2
                        self.y -= self.velocidade
                        return
                elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                        self.direcao = 1
                        self.x -= self.velocidade
                        return
                if not self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                    self.direcao = random.choice([1,2,3])
<<<<<<< HEAD
                    #print("embaralhei a direçaõ no 0")
=======
>>>>>>> 8639339 (add code documentation)
                    return
            elif self.direcao == 1:
                if  self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    self.direcao = 1
                    self.x -= 1
                    return 
                elif self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                    self.direcao = 3
                    self.y += self.velocidade
                    return
                elif  self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                    self.direcao = 2
                    self.y -= self.velocidade
                else:
                    self.x += self.velocidade
                    return
                if not self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    self.direcao = random.choice([0,2,3])
<<<<<<< HEAD
                    #print("embaralhei a direçaõ no 1")
=======
>>>>>>> 8639339 (add code documentation)
            elif self.direcao == 2:
                if self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                    self.direcao = 2
                    self.y -= self.velocidade
                    return
                elif self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                        self.direcao = 0
                        self.x += self.velocidade
                        return
                elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                        self.direcao = 1
                        self.x -= self.velocidade
                        return
                else:
                        self.y += self.velocidade
                if not self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                    self.direcao = random.choice([0,1,3])
<<<<<<< HEAD
                    #print("embaralhei a direção no 2")
=======
>>>>>>> 8639339 (add code documentation)
            elif self.direcao == 3:
                if self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                    self.y += self.velocidade
                    return
                elif self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                        self.direcao = 0
                        self.x += self.velocidade
                        return
                elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                        self.direcao = 1
                        self.x -= self.velocidade
                else:
                        self.y -= self.velocidade
                if not self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                    self.direcao = random.choice([0,1,2])
<<<<<<< HEAD
                    #print("embaralhei no 3")
=======
                    
>>>>>>> 8639339 (add code documentation)
                    