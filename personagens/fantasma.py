import pygame 
from pygame import Surface
from imagens.imagem import Imagem
<<<<<<< HEAD
#Superclasse com os métodos compartilhados dos fantasmas. Os 4 herdam dela
class Fantasma: 
=======

class Fantasma: 

    """
    Superclasse responsável por definir o comportamento base de todos os
    fantasmas do jogo.

    Esta classe centraliza atributos e funcionalidades compartilhadas entre
    Blink, Inky, Clyde e Pynk, como movimentação no labirinto, controle de
    animação, estados de medo, saída da casinha e verificação de colisões
    com o tabuleiro.

    A partir dessa classe, cada fantasma especializado implementa sua
    própria estratégia de movimentação, reutilizando a lógica comum e
    garantindo organização, reutilização de código e facilidade de
    manutenção do projeto.
    """

>>>>>>> 8639339 (add code documentation)
    def __init__(self, imagem : Imagem, velocidade: float = 2.8):
        pygame.init()
        self.__x = 0
        self.__y = 0
        self.__imagem = imagem
        self.__taxa_animacao = 0
        self.__velocidade = velocidade
        self.__direcoes = {0: (1, 0), 1: (-1, 0), 2: (0, -1), 3: (0, 1)}
        self.__sair_casinha = False
        self.__fantasma_saiu = False
        self.__tempo_retorno = None
        self.__direcao = 0
        self.__fantasma_medroso = False
        self.__lista_imagens = []

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
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, value):
        self.__imagem = value

    @property
    def taxa_animacao(self):
        return self.__taxa_animacao

    @taxa_animacao.setter
    def taxa_animacao(self, value):
        self.__taxa_animacao = value

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, value):
        self.__velocidade = value

    @property
    def direcoes(self):
        return self.__direcoes

    @direcoes.setter
    def direcoes(self, value):
        self.__direcoes = value

    @property
    def sair_casinha(self):
        return self.__sair_casinha

    @sair_casinha.setter
    def sair_casinha(self, value):
        self.__sair_casinha = value

    @property
    def fantasma_saiu(self):
        return self.__fantasma_saiu

    @fantasma_saiu.setter
    def fantasma_saiu(self, value):
        self.__fantasma_saiu = value

    @property
    def tempo_retorno(self):
        return self.__tempo_retorno

    @tempo_retorno.setter
    def tempo_retorno(self, value):
        self.__tempo_retorno = value

    @property
    def direcao(self):
        return self.__direcao

    @direcao.setter
    def direcao(self, value):
        self.__direcao = value

    @property
    def fantasma_medroso(self):
        return self.__fantasma_medroso

    @fantasma_medroso.setter
    def fantasma_medroso(self, value):
        self.__fantasma_medroso = value

    @property
    def lista_imagens(self):
        return self.__lista_imagens

    @lista_imagens.setter
    def lista_imagens(self, value):
        self.__lista_imagens = value

    def controlar_medo(self, medroso: bool) -> None:
        if medroso:
            self.fantasma_medroso = True
        else:
            self.fantasma_medroso = False

    def inicializar_posicao(self, x: int, y: int) -> None:
        self.x = x * 16
        self.y = y * 18

    def voltar_casinha (self, x:int, y:int) -> None:
        self.fantasma_medroso = False
        self.inicializar_posicao(x, y)
        self.sair_casinha = False
        self.fantasma_saiu = False
        self.tempo_retorno= pygame.time.get_ticks()

    def desenhar_fantasma(self, tela: Surface, x: int, y: int) -> None: 
        if self.fantasma_medroso:
            img = self.imagem.indefeso_img[self.taxa_animacao // 5]
        else:
            img = self.lista_imagens[self.taxa_animacao // 10]
        tela.blit(img, (x, y))

    def controlar_animacao(self) -> None:
        if self.taxa_animacao < 25:
            self.taxa_animacao +=1
        else:
            self.taxa_animacao = 0

    def liberar_fantasma(self, tempo_jogo: int, tempo_liberacao : int) -> None:
        if self.tempo_retorno is None:
            if tempo_jogo > tempo_liberacao:
                self.sair_casinha = True
        else:
            if tempo_jogo - self.tempo_retorno > 3000:
                self.sair_casinha = True
                self.tempo_retorno = None

    def sair_da_casinha(self, deslocar: int, altura: int, tabuleiro: list, celula_largura: int, celula_altura: int) -> tuple:
        if not self.sair_casinha:
            return self.x, self.y 

        if self.y > altura:
            direcao = 2  
        elif self.y < altura:
            direcao = 3 
        elif self.x > deslocar:
            direcao = 1
        elif self.x < deslocar:
            direcao = 0 
        else:
            return self.x

        dir_x, dir_y = self.direcoes[direcao]
        novo_x = self.x + dir_x * self.velocidade
        novo_y = self.y + dir_y * self.velocidade

        coluna = int((novo_x + celula_largura // 2) // celula_largura)
        linha = int((novo_y + celula_altura // 2) // celula_altura)
        if 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]):
            valor = tabuleiro[linha][coluna]
            if valor in (0, 1, 2, 9): 
                return novo_x, novo_y       
        return self.x, self.y #não conseguiu se mover

    def pode_mover(self, direcao: int, tabuleiro: list, celula_largura: int, celula_altura: int) -> bool:
        dir_x, dir_y = self.direcoes[direcao]
        novo_x = self.x + dir_x * self.velocidade
        novo_y = self.y + dir_y * self.velocidade 

        coluna = int((novo_x + celula_largura // 2) // celula_largura)
        linha = int((novo_y + celula_altura // 2) // celula_altura)

        if 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]):
            valor = tabuleiro[linha][coluna]
            if valor in (0,1,2): #o fantasma não pode retornar para dentro
                return True

        return False
   
    def fugir (self, direcao: int, x_pac : int, y_pac : int, tabuleiro: list, celula_largura, celula_altura) -> tuple:
        alvo_pacman = [x_pac, y_pac]

        if direcao == 1:
            if alvo_pacman[0] > self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                self.x -= self.velocidade
            elif not self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                if alvo_pacman[1] > self.y and self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                    direcao = 2
                    self.y -= self.velocidade
                elif alvo_pacman[1] < self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                    direcao = 3
                    self.y += self.velocidade
                elif alvo_pacman[0] < self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                    direcao = 0
                    self.x += self.velocidade
                elif self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                    direcao = 3
                    self.y += self.velocidade
                elif self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                    direcao = 2
                    self.y -= self.velocidade
                elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    direcao = 1
                    self.x -= self.velocidade
            elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                if alvo_pacman[1] > self.y and self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                    direcao = 2
                    self.y -= self.velocidade 
                if alvo_pacman[1] < self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                    direcao = 3
                    self.y += self.velocidade
                else:
                    self.x -= self.velocidade
        elif direcao == 0:
            if alvo_pacman[1] > self.y and self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                direcao = 2
                self.y += self.velocidade
            elif alvo_pacman[0] < self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                self.x += self.velocidade
            elif not self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                if alvo_pacman[1] > self.y and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    direcao = 2
                    self.y -= self.velocidade
                elif alvo_pacman[1] < self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                    direcao = 3
                    self.y += self.velocidade
                elif alvo_pacman[0] > self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    direcao = 1
                    self.x -= self.velocidade
                elif self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                    direcao = 3
                    self.y += self.velocidade
                elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    direcao = 2
                    self.y -= self.velocidade
                elif self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                    direcao = 0
                    self.x -= self.velocidade
            elif self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                if alvo_pacman[1] > self.y and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    direcao = 2
                    self.y -= self.velocidade
                if alvo_pacman[1] < self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                    direcao = 3
                    self.y += self.velocidade
                else:
                    self.x += self.velocidade
                    
        elif direcao == 3:
            if alvo_pacman[0] < self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                direcao = 0
                self.x += self.velocidade
            elif alvo_pacman[1] < self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                direcao = 3
                self.y += self.velocidade
            elif not self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                if alvo_pacman[0] > self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    direcao = 1
                    self.x -= self.velocidade
                elif alvo_pacman[0] < self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                    direcao = 0
                    self.x += self.velocidade
                elif alvo_pacman[1] > self.y and self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                    direcao = 2
                    self.y -= self.velocidade
                elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    direcao = 1
                    self.x -= self.velocidade
                elif self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                    direcao = 3
                    self.y += self.velocidade
                elif self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                    direcao = 0
                    self.x += self.velocidade
            elif self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                if alvo_pacman[0] > self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    direcao = 1
                    self.x -= self.velocidade
                elif alvo_pacman[0] < self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                    direcao = 0
                    self.x += self.velocidade
                else:
                    self.y -= self.velocidade
        elif direcao == 2:
            if alvo_pacman[1] > self.y and self.pode_mover(2, tabuleiro, celula_largura, celula_altura):
                self.y -= self.velocidade
            elif not self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                if alvo_pacman[0] > self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    direcao = 1
                    self.x -= self.velocidade
                elif alvo_pacman[0] < self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                    direcao = 0
                    self.x += self.velocidade
                elif alvo_pacman[1] < self.y and self.pode_mover(3, tabuleiro, celula_largura, celula_altura):
                    direcao = 3
                    self.y += self.velocidade
                elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    direcao = 2
                    self.y -= self.velocidade
                elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    direcao = 1
                    self.x -= self.velocidade
                elif self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                    direcao = 0
                    self.x += self.velocidade
            elif self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                if alvo_pacman[0] > self.x and self.pode_mover(1, tabuleiro, celula_largura, celula_altura):
                    direcao = 1
                    self.x -= self.velocidade
                elif alvo_pacman[0] < self.x and self.pode_mover(0, tabuleiro, celula_largura, celula_altura):
                    direcao = 0
                    self.x += self.velocidade
                else:
                    self.y += self.velocidade
<<<<<<< HEAD
=======
        return self.x, self.y, self.direcao
>>>>>>> 8639339 (add code documentation)

        