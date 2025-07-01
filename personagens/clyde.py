from personagens.fantasma import Fantasma
import pygame

class Clyde(Fantasma):
    def __init__(self, imagem, velocidade = 1.3):
        super().__init__(imagem, velocidade)
        pygame.init()
        self.lista_imagens = self.imagem.clyde_img

    def mover(self, pacman_poderoso: bool, x_pac: int, y_pac: int, tabuleiro: list, celula_largura: int, celula_altura: int) -> None:
        if not self.fantasma_saiu: 
            self.x , self.y = self.sair_da_casinha(256, 16, tabuleiro , celula_largura, celula_altura)
            if round(self.y) == 216: 
                self.fantasma_saiu = True
            return

        if pacman_poderoso:
           self.x, self.y , self.direcao=  self.fugir(self.direcao,x_pac, y_pac, tabuleiro, celula_largura, celula_altura)
           return
        else:
            distancia = ((x_pac - self.x)**2 + (y_pac - self.y) **2) **0.5

            estado = "perseguindo" 
            if distancia <= 50:
                estado = "fugindo"
            elif distancia > 300:
                estado = "perseguindo"

            if estado == "perseguindo":
                alvo_pacman = (x_pac, y_pac)
            
                if self.direcao == 0:
                    if alvo_pacman[0] > self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                        self.x += self.velocidade
                    elif not self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                        if alvo_pacman[1] > self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 3
                            self.y += self.velocidade
                        elif alvo_pacman[1] < self.y and self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 2
                            self.y -= self.velocidade
                        elif alvo_pacman[0] < self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 1
                            self.x -= self.velocidade
                        elif self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 3
                            self.y += self.velocidade
                        elif self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 2
                            self.y -= self.velocidade
                        elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 1
                            self.x -= self.velocidade
                    elif self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                        if alvo_pacman[1] > self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 3
                            self.y += self.velocidade
                        if alvo_pacman[1] < self.y and self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 2
                            self.y -= self.velocidade
                        else:
                            self.x += self.velocidade
                elif self.direcao == 1:
                    if alvo_pacman[1] > self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                        self.direcao = 3
                    elif alvo_pacman[0] < self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                        self.x -= self.velocidade
                    elif not self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                        if alvo_pacman[1] > self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 3
                            self.y += self.velocidade
                        elif alvo_pacman[1] < self.y and self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 2
                            self.y -= self.velocidade
                        elif alvo_pacman[0] > self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 0
                            self.x += self.velocidade
                        elif self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 3
                            self.y += self.velocidade
                        elif self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 2
                            self.y -= self.velocidade
                        elif self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 0
                            self.x += self.velocidade
                    elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                        if alvo_pacman[1] > self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 3
                            self.y += self.velocidade
                        if alvo_pacman[1] < self.y and self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 2
                            self.y -= self.velocidade
                        else:
                            self.x -= self.velocidade
                elif self.direcao == 2:
                    if alvo_pacman[0] < self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                        self.direcao = 1
                        self.x -= self.velocidade
                    elif alvo_pacman[1] < self.y and self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                        self.direcao = 2
                        self.y -= self.velocidade
                    elif not self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                        if alvo_pacman[0] > self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 0
                            self.x += self.velocidade
                        elif alvo_pacman[0] < self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 1
                            self.x -= self.velocidade
                        elif alvo_pacman[1] > self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 3
                            self.y += self.velocidade
                        elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 1
                            self.x -= self.velocidade
                        elif self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 3
                            self.y += self.velocidade
                        elif self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 0
                            self.x += self.velocidade
                    elif self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                        if alvo_pacman[0] > self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 0
                            self.x += self.velocidade
                        elif alvo_pacman[0] < self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 1
                            self.x -= self.velocidade
                        else:
                            self.y -= self.velocidade
                elif self.direcao == 3:
                    if alvo_pacman[1] > self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                        self.y += self.velocidade
                    elif not self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                        if alvo_pacman[0] > self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 0
                            self.x += self.velocidade
                        elif alvo_pacman[0] < self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 1
                            self.x -= self.velocidade
                        elif alvo_pacman[1] < self.y and self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 2
                            self.y -= self.velocidade
                        elif self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 2
                            self.y -= self.velocidade
                        elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 1
                            self.x -= self.velocidade
                        elif self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 0
                            self.x += self.velocidade
                    elif self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                        if alvo_pacman[0] > self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 0
                            self.x += self.velocidade
                        elif alvo_pacman[0] < self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                            self.direcao = 1
                            self.x -= self.velocidade
                        else:
                            self.y += self.velocidade

            elif estado == 'fugindo':
                self.x, self.y , self.direcao = self.fugir(self.direcao,x_pac, y_pac, tabuleiro, celula_largura, celula_altura)
            else :
                self.x, self.y , self.direcao = self.fugir(self.direcao, x_pac, y_pac, tabuleiro, celula_largura, celula_altura)
            