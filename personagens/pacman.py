
import pygame
import sys
import os
from pygame import Surface
from imagens.imagem import Imagem
from personagens.tangerina import Tangerina
from personagens.fantasma import Fantasma

class Pacman:
<<<<<<< HEAD
=======

    """
    Classe responsável por representar o personagem Pac-Man e centralizar
    toda a lógica relacionada ao jogador.

    Esta classe controla o estado do Pac-Man, incluindo posição em pixels,
    direção atual, animações, pontuação, vidas e estados especiais como
    poder temporário e morte.

    Também é responsável por gerenciar movimentação no tabuleiro,
    interação com bolinhas, superpoderes, fantasmas e itens especiais,
    além de lidar com colisões e regras principais da jogabilidade.
    """

>>>>>>> 8639339 (add code documentation)
    def __init__(self, imagem: Imagem, velocidade: float = 1.5):
        self.__inicializar()
        self.__imagem = imagem
        self.__direcao = 0
        self.__direcao_comando = 0
        self.__taxa_animacao = 0
        self.__velocidade = velocidade
        self.__direcoes = {0: (1, 0), 1: (-1, 0), 2: (0, -1), 3: (0, 1) }
        self.__x_pixels = 0
        self.__y_pixels = 0
        self.__pontuação = 0
        self.__vidas = 3
        self.__pacman_poderoso = False
        self.__inicio_poder = 0
        self.__pacman_morto = False
        self.__tempo_morte = 0
        
    @property
    def x_pixels(self):
        return self.__x_pixels

    @x_pixels.setter
    def x_pixels(self, value):
        self.__x_pixels = value

    @property
    def y_pixels(self):
        return self.__y_pixels

    @y_pixels.setter
    def y_pixels(self, value):
        self.__y_pixels = value

    @property
    def pontuação(self):
        return self.__pontuação

    @pontuação.setter
    def pontuação(self, value):
        self.__pontuação = value

    @property
    def vidas(self):
        return self.__vidas

    @vidas.setter
    def vidas(self, value):
        self.__vidas = value

    @property
    def pacman_poderoso(self):
        return self.__pacman_poderoso

    @pacman_poderoso.setter
    def pacman_poderoso(self, value):
        self.__pacman_poderoso = value

    @property
    def inicio_poder(self):
        return self.__inicio_poder

    @inicio_poder.setter
    def inicio_poder(self, value):
        self.__inicio_poder = value

    @property
    def pacman_morto(self):
        return self.__pacman_morto

    @pacman_morto.setter
    def pacman_morto(self, value):
        self.__pacman_morto = value

    @property
    def tempo_morte(self):
        return self.__tempo_morte

    @tempo_morte.setter
    def tempo_morte(self, value):
        self.__tempo_morte = value

    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem

    @property
    def direcao(self):
        return self.__direcao

    @direcao.setter
    def direcao(self, direcao):
        self.__direcao = direcao

    @property
    def direcao_comando(self):
        return self.__direcao_comando

    @direcao_comando.setter
    def direcao_comando(self, direcao_comando):
        self.__direcao_comando = direcao_comando

    @property
    def taxa_animacao(self):
        return self.__taxa_animacao

    @taxa_animacao.setter
    def taxa_animacao(self, taxa_animacao):
        self.__taxa_animacao = taxa_animacao

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    @property
    def direcoes(self):
        return self.__direcoes

    @direcoes.setter
    def direcoes(self, direcoes):
        self.__direcoes = direcoes
    
    def __inicializar(self) -> None:
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'imagens')))
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    def inicializar_posicao_pacman(self):
        self.x_pixels = 2 * 16 #ja posso inicializar la em cima mesmo
        self.y_pixels = 28 *18

    def desenhar_pacman(self, tela: Surface):
        self.imagem.carregar_imagens()
        x = self.x_pixels
        y = self.y_pixels
        if self.pacman_morto:
            tela.blit(self.imagem.pacman_morto[self.taxa_animacao//14], (x, y))
        else:
            img = self.imagem.jogador_img[self.taxa_animacao // 2]
            if self.direcao == 0:
                tela.blit(img, (x, y))
            elif self.direcao == 1:
                tela.blit(pygame.transform.flip(img, True, False), (x, y))
            elif self.direcao == 2:
                tela.blit(pygame.transform.rotate(img, 90), (x, y))
            elif self.direcao == 3:
                tela.blit(pygame.transform.rotate(img, 270), (x, y))

    def controlar_animacao(self):
        if self.taxa_animacao < 200:
            self.taxa_animacao +=1
        else:
            self.taxa_animacao = 0

    def controlar_movimento(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN and not self.pacman_morto:
            if event.key == pygame.K_RIGHT:
                self.direcao_comando = 0
            elif event.key == pygame.K_LEFT:
                self.direcao_comando = 1
            elif event.key == pygame.K_UP:
                self.direcao_comando = 2
            elif event.key == pygame.K_DOWN:
                self.direcao_comando = 3

    def pode_mover(self, direcao: int, tabuleiro: list, celula_largura: int, celula_altura: int) -> bool:

        incrementar_coluna, incrementar_linha = self.direcoes[direcao]
        novo_x = self.x_pixels + incrementar_coluna * self.velocidade
        novo_y = self.y_pixels + incrementar_linha * self.velocidade

        nova_coluna = int((novo_x + celula_largura //2)// celula_largura)
        nova_linha = int((novo_y + celula_altura //2) // celula_altura)

        if 0 <= nova_linha < len(tabuleiro) and 0 <= nova_coluna < len(tabuleiro[0]):
            return tabuleiro[nova_linha][nova_coluna] < 3
        return False

    def mover(self, tabuleiro: list, celula_largura: int, celula_altura: int) -> None:
        if self.pode_mover(self.direcao_comando, tabuleiro, celula_largura, celula_altura) and not self.pacman_morto: #agora ele não anda mais quando morre
            self.direcao = self.direcao_comando
        if self.pode_mover(self.direcao, tabuleiro, celula_largura, celula_altura) and not self.pacman_morto:
            #self.direcao = self.direcao_comando
            incrementar_coluna, incrementar_linha = self.direcoes[self.direcao]
            self.x_pixels += incrementar_coluna * self.velocidade
            self.y_pixels += incrementar_linha * self.velocidade

    def comer_bolinhas (self, tabuleiro: list, todas_bolinhas: int,celula_largura: int, celula_altura: int, fantasmas: list) -> tuple:
        coluna = int((self.x_pixels + celula_largura //2) // celula_largura) 
        linha = int((self.y_pixels + celula_altura // 2) // celula_altura)
        if 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]):
            if tabuleiro[linha][coluna] == 1:
                self.pontuação += 10
                tabuleiro[linha][coluna] = 0 
                todas_bolinhas -=1
                return todas_bolinhas, "comer_bolinhas"
            elif tabuleiro[linha][coluna] == 2:
                self.pontuação += 15 
                tabuleiro[linha][coluna] = 0
                todas_bolinhas -= 1
                self.ativar_poder(fantasmas) 
                return todas_bolinhas, "superpoder"
        return todas_bolinhas, "nada"

    def ativar_poder(self, fantasmas: list) -> None:
        self.pacman_poderoso = True
        self.inicio_poder = pygame.time.get_ticks()
        for fantasma in fantasmas:
            fantasma.controlar_medo(True)

    def desativar_poder(self, fantasmas: list) -> None:
        if self.pacman_poderoso:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.inicio_poder >= 10000:  #10 segundos
                self.pacman_poderoso = False
                for fantasma in fantasmas:
                    fantasma.controlar_medo(False)

    def __le__(self, objeto: any) -> bool: 
        distancia = ((self.x_pixels - objeto.x)**2 + (self.y_pixels - objeto.y)**2)**0.5
        return distancia <= 12

    def verificar_colisao(self,fantasma: Fantasma, fantasmas: list,x:int, y: int) -> str:
        if self <= fantasma:
            if self.pacman_poderoso:
                self.pontuação += 20
                fantasma.voltar_casinha(x, y)
                return "comer_fantasma"
            else:
                self.pacman_morto = True
                self.tempo_morte = pygame.time.get_ticks()
                self.inicializar_posicao_pacman()
                pygame.display.update()
                self.vidas -= 1
                posicoes_iniciais = [(13,14), (14,14), (15,14), (16,14)]
                for nome, (x, y) in zip(fantasmas, posicoes_iniciais):
                    nome.voltar_casinha(x,y)
                return "morrer"
        return "nada"
    
    def reviver_pacman (self) -> None:
        if pygame.time.get_ticks() -  self.tempo_morte >= 3000 and self.vidas >=0:
            if self.pacman_morto and self.vidas >=1: #só revivo até 3 vidas
                self.pacman_morto = False
                self.direcao = 0
                self.inicializar_posicao_pacman()

    def comer_tangerina(self, tangerina: Tangerina) -> bool:
        if self <= tangerina and tangerina.ativa:
            if self.vidas < 3:
                self.vidas += 1
            tangerina.desaparecer(True) 
            self.pontuação += 50 
            return True
               