import pygame
from pygame.locals import QUIT
import sys
import os
import json
from desenvolvimento.cena import Cena
from desenvolvimento.tela import Tela
from personagens.pacman import Pacman
from cenario.labirinto import Labirinto
from som.audio import Audio
from personagens.blink import Blink
from personagens.clyde import Clyde
from personagens.inky import Inky
from personagens.pynk import Pynk
from personagens.tangerina import Tangerina
from imagens.imagem import Imagem

class Jogo:
<<<<<<< HEAD
=======

    """
    Classe principal responsável por gerenciar o ciclo completo do jogo.

    Esta classe atua como o núcleo da aplicação, coordenando a interação
    entre todos os componentes do jogo, como cenário (labirinto),
    personagens (Pac-Man, fantasmas e itens), áudio, imagens, telas e cenas.
    Ela controla o loop principal do jogo, o fluxo de estados (rodando,
    pausado, fim de jogo), além de eventos de teclado e atualização gráfica.

    Também é responsável por inicializar posições, reiniciar partidas,
    salvar e carregar o estado do jogo em arquivo, garantindo a continuidade
    da partida, e por sincronizar lógica, animações, colisões e sons durante
    a execução.
    """

>>>>>>> 8639339 (add code documentation)
    def __init__(self) -> None:
        pygame.init()
        self.__inicializar()
        self.__esta_rodando = True
        self.__imagem = Imagem()
        self.__labirinto = Labirinto()
        self.__tela = Tela()
        self.__pause = False
        self.__pacman = Pacman(self.imagem)
        self.__audio = Audio()
        self.__blink = Blink(self.imagem)
        self.__clyde = Clyde(self.imagem)
        self.__inky = Inky(self.imagem)
        self.__pynk = Pynk(self.imagem)
        self.__tempo_jogo = 0
        self.__fim_jogo = False
        self.__tangerina = Tangerina(self.imagem)
        self.__cena = Cena(self.imagem)
        self.inicializar_posicoes()
        self.imagem.carregar_imagens()
        
    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, value):
        self.__imagem = value

    @property
    def tangerina(self):
        return self.__tangerina

    @tangerina.setter
    def tangerina(self, value):
        self.__tangerina = value

    @property
    def pacman(self):
        return self.__pacman

    @pacman.setter
    def pacman(self, value):
        self.__pacman = value

    @property
    def pause(self):
        return self.__pause

    @pause.setter
    def pause(self, pause):
        self.__pause = pause

    @property
    def audio(self):
        return self.__audio

    @audio.setter
    def audio(self, value):
        self.__audio = value

    @property
    def blink(self):
        return self.__blink

    @blink.setter
    def blink(self, value):
        self.__blink = value

    @property
    def clyde(self):
        return self.__clyde

    @clyde.setter
    def clyde(self, value):
        self.__clyde = value

    @property
    def inky(self):
        return self.__inky

    @inky.setter
    def inky(self, value):
        self.__inky = value

    @property
    def pynk(self):
        return self.__pynk

    @pynk.setter
    def pynk(self, value):
        self.__pynk = value

    @property
    def tempo_jogo(self):
        return self.__tempo_jogo

    @tempo_jogo.setter
    def tempo_jogo(self, value):
        self.__tempo_jogo = value

    @property
    def fim_jogo(self):
        return self.__fim_jogo

    @fim_jogo.setter
    def fim_jogo(self, value):
        self.__fim_jogo = value

    @property
    def tela(self):
        return self.__tela

    @tela.setter
    def tela(self, tela):
        self.__tela = tela

    @property
    def esta_rodando(self):
        return self.__esta_rodando

    @esta_rodando.setter
    def esta_rodando(self, esta_rodando):
        self.__esta_rodando = esta_rodando

    @property
    def labirinto(self):
        return self.__labirinto

    @labirinto.setter
    def labirinto(self, labirinto):
        self.__labirinto = labirinto

    @property
    def cena(self):
        return self.__cena
    
    @cena.setter
    def cena(self, cena):
        self.__cena = cena

    @property
    def esta_rodando(self):
        return self.__esta_rodando 

    @esta_rodando.setter
    def esta_rodando(self, esta_rodando):
        self.__esta_rodando = esta_rodando

    def __inicializar(self) -> None:
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'cenario')))
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'personagens')))

    def inicializar_posicoes (self) -> None:
        self.blink.inicializar_posicao(13, 14)
        self.inky.inicializar_posicao(15, 14)
        self.pynk.inicializar_posicao(14,14)
        self.clyde.inicializar_posicao(16,14)
        self.pacman.inicializar_posicao_pacman()

    def reiniciar(self) -> None:
        self.cena.mostrar_tela_start(self.tela.tela, self.audio)
        self.tempo_jogo = 0
        self.pacman.vidas = 3
        self.labirinto.todas_bolinhas = 246
        self.pacman.pacman_morto = False
        self.pacman.tempo_morte = 0
        self.pacman.pacman_poderoso = False
        self.pacman.pontuação = 0
        self.inicializar_posicoes()
        self.audio.parar_som_sirene()
        self.tangerina.ativa = True

        nomes = ['blink', 'inky', 'pynk', 'clyde']
        for nome in nomes:
            fantasma = getattr(self, nome)
            fantasma.sair_casinha = False
            fantasma.fantasma_saiu = False
            fantasma.tempo_retorno = pygame.time.get_ticks()
            fantasma.fantasma_medroso = False

        self.pacman.pacman_poderoso = False
        self.pause = False
        self.fim_jogo = False
        self.labirinto.tabuleiro = [[6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
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
        [3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
        [3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
        [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
        [3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
        [7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
                ]

    def salvar_jogo(self) -> None:
        estado = {
            "pacman" : {
                "x": self.pacman.x_pixels,
                "y": self.pacman.y_pixels,
                "vidas": self.pacman.vidas,
                "pontuacao": self.pacman.pontuação,
                "morto": self.pacman.pacman_morto,
                "poderoso": self.pacman.pacman_poderoso,
                "inicio_poder": self.pacman.inicio_poder,
                "tempo_morte": self.pacman.tempo_morte
            },
            "labirinto":{
                 "tabuleiro" : self.labirinto.tabuleiro,
                 "todas_bolinhas" : self.labirinto.todas_bolinhas
            },
            "fantasmas": {
                "blink": {
                    "x": self.blink.x,
                    "y": self.blink.y,
                    "saiu": self.blink.fantasma_saiu,
                    "sair_casinha": self.blink.sair_casinha,
                    "tempo_retorno": self.blink.tempo_retorno,
                    "medroso": self.blink.fantasma_medroso
                },
                "inky":{
                    "x": self.inky.x,
                    "y": self.inky.y,
                    "saiu": self.inky.fantasma_saiu,
                    "sair_casinha": self.inky.sair_casinha,
                    "tempo_retorno": self.inky.tempo_retorno,
                    "medroso": self.inky.fantasma_medroso
                },
                "pynk": {
                    "x": self.pynk.x,
                    "y": self.pynk.y,
                    "saiu": self.pynk.fantasma_saiu,
                    "sair_casinha": self.pynk.sair_casinha,
                    "tempo_retorno": self.pynk.tempo_retorno,
                    "medroso": self.pynk.fantasma_medroso
                },
                "clyde":{
                    "x": self.clyde.x,
                    "y": self.clyde.y,
                    "saiu": self.clyde.fantasma_saiu,
                    "sair_casinha": self.clyde.sair_casinha,
                    "tempo_retorno": self.clyde.tempo_retorno,
                    "medroso": self.clyde.fantasma_medroso
                }
            },
            "tempo" : self.tempo_jogo,
            "tempo_audio": self.audio.inicio_audio,

            "tangerina": {
                "x": self.tangerina.x,
                "y": self.tangerina.y,
                "ativa": self.tangerina.ativa
            }
        }
        with open ("save.json", "w") as arquivo:
            json.dump(estado, arquivo)

    def carregar_jogo(self) -> None:
        import traceback
        try:
            with open("save.json", "r") as arquivo:
                estado = json.load(arquivo)

            self.pacman.x_pixels = estado["pacman"]["x"]
            self.pacman.y_pixels = estado["pacman"]["y"]
            self.pacman.vidas = estado["pacman"]["vidas"]
            self.pacman.pacman_poderoso = estado["pacman"]["poderoso"]
            self.pacman.inicio_poder = estado["pacman"]["inicio_poder"]
            self.pacman.pacman_morto = estado["pacman"]["morto"]
            self.pacman.tempo_morte = estado["pacman"]["tempo_morte"]
            self.pacman.pontuação = estado["pacman"]["pontuacao"]
            self.labirinto.tabuleiro = estado["labirinto"]["tabuleiro"]
            self.labirinto.todas_bolinhas = estado["labirinto"]["todas_bolinhas"]
            self.tempo_jogo = estado["tempo"]
            self.audio.inicio_audio = estado["tempo_audio"]
            self.tangerina.x = estado["tangerina"]["x"]
            self.tangerina.y = estado["tangerina"]["y"]
            self.tangerina.ativa = estado["tangerina"]["ativa"]

            for nome in ["blink", "inky", "pynk", "clyde"]:
                fantasma = getattr(self, nome)
                dados = estado["fantasmas"][nome]
                fantasma.x = dados["x"]
                fantasma.y = dados["y"]
                fantasma.fantasma_saiu = dados["saiu"]
                fantasma.sair_casinha = dados ["sair_casinha"]
                fantasma.tempo_retorno = dados["tempo_retorno"]
                fantasma.fantasma_medroso = dados["medroso"]

        except (FileNotFoundError, KeyError, json.JSONDecodeError) as erro:
            print("Não foi possível carregar o jogo salvo.")
            print(f"Erro: {erro}")
            traceback.print_exc()

    def rodar(self) -> None:
        if self.cena.mostrar_tela_start(self.tela.tela, self.audio):
            self.carregar_jogo()

        while self.esta_rodando:
            self.tela.tela.fill((0,0,0))

            eventos = pygame.event.get()

            for event in eventos:
                if event.type == QUIT:
                    self.salvar_jogo()
                    pygame.quit()
                    self.esta_rodando = False
                    sys.exit()
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_p: # se for s tem que salvar e sair, r resetar
                        self.pause = not self.pause
                    elif self.pause or self.fim_jogo:
    
                        if event.key == pygame.K_r:
                            self.reiniciar()
                        elif event.key == pygame.K_s:
                            self.salvar_jogo()
                            self.esta_rodando = False
                            sys.exit()
                if not self.pause:
                    self.pacman.controlar_movimento(event)

            if self.pause:
                self.tela.tela.fill((0,0,0))
                self.cena.desenhar_configuracoes(self.tela.tela)
                pygame.display.flip()
                self.audio.parar_som_sirene()
            else:
                self.tempo_jogo = pygame.time.get_ticks()
                self.cena.relogio.tick(self.cena.fps)
                self.labirinto.desenhar_tabuleiro(self.tela.tela, self.tela.celula_largura, self.tela.celula_altura) 
                self.pacman.desenhar_pacman(self.tela.tela)
                self.clyde.desenhar_fantasma(self.tela.tela, self.clyde.x, self.clyde.y)
                self.inky.desenhar_fantasma(self.tela.tela,self.inky.x, self.inky.y)
                self.blink.desenhar_fantasma(self.tela.tela, self.blink.x, self.blink.y)
                self.pynk.desenhar_fantasma(self.tela.tela,self.pynk.x,self.pynk.y)
                self.audio.parar_musica_superpoder()
                self.cena.mostrar_pontuação(self.pacman.pontuação, self.tela.tela)
                self.cena.contar_vidas(self.pacman.vidas, self.tela.tela)
                self.pacman.controlar_animacao()
                self.pacman.mover(self.labirinto.tabuleiro, self.tela.celula_largura, self.tela.celula_altura)
                self.blink.controlar_animacao()
                self.pynk.controlar_animacao()
                self.inky.controlar_animacao()
                self.clyde.controlar_animacao()
                self.tangerina.desenhar_tangerina(self.tela.tela)

                comeu_tangerina = self.pacman.comer_tangerina(self.tangerina)
                self.tangerina.desaparecer(comeu_tangerina)
                if comeu_tangerina:
                    self.audio.ouvir_comer_tangerina()
                self.labirinto.todas_bolinhas, resultado = self.pacman.comer_bolinhas(self.labirinto.tabuleiro, self.labirinto.todas_bolinhas, self.tela.celula_largura, self.tela.celula_altura,[self.blink, self.pynk, self.inky, self.clyde])
                if resultado == 'comer_bolinhas':
                    self.audio.ouvir_comer_bolinhas()
                elif resultado == 'superpoder':
                    self.audio.ouvir_superpoder()
                self.labirinto.piscar_bolinha()
                self.pacman.desativar_poder([self.blink, self.pynk, self.inky, self.clyde])
                self.fim_jogo = self.cena.desenhar_tela_final(self.labirinto.todas_bolinhas, self.pacman.vidas, self.tela.tela, self.audio)
                if not self.fim_jogo :
                    self.blink.liberar_fantasma(self.tempo_jogo, 3000) 
                    self.clyde.liberar_fantasma(self.tempo_jogo, 6000)
                    self.inky.liberar_fantasma(self.tempo_jogo, 9000)
                    self.pynk.liberar_fantasma(self.tempo_jogo, 12000)
                    self.audio.som_sirene(self.pacman.pacman_morto)
                    self.pacman.reviver_pacman()
                    self.blink.mover(self.pacman.pacman_poderoso, self.pacman.x_pixels, self.pacman.y_pixels,self.labirinto.tabuleiro, self.tela.celula_largura, self.tela.celula_altura)
                    self.clyde.mover(self.pacman.pacman_poderoso, self.pacman.x_pixels, self.pacman.y_pixels,self.labirinto.tabuleiro, self.tela.celula_largura, self.tela.celula_altura)
                    self.inky.mover(self.pacman.pacman_poderoso, self.pacman.x_pixels, self.pacman.y_pixels,self.tela.celula_largura, self.tela.celula_altura, self.labirinto.tabuleiro)
                    self.pynk.mover(self.pacman.pacman_poderoso, self.pacman.x_pixels, self.pacman.y_pixels , self.pacman.direcao,self.labirinto.tabuleiro,self.tela.celula_largura, self.tela.celula_altura)
                    for fantasma, (x, y) in zip([self.blink, self.inky, self.pynk, self.clyde],[(13, 14), (14, 14), (15, 14), (16, 14)]):
                        resultado = self.pacman.verificar_colisao(fantasma, [self.blink, self.inky, self.pynk, self.clyde], x, y)
                        if resultado == "comer_fantasma":
                            self.audio.comer_fantasma()
                        elif resultado == "morrer":
                            self.audio.morrer()
                            self.audio.som_sirene(True)

                pygame.display.flip()
