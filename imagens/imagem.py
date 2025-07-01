import pygame
import os

class Imagem:
    def __init__(self) -> None:
        pygame.init()
        self.__start_logo = ""
        self.__jogador_img = []
        self.__diretorio_atual = os.path.dirname(__file__)
        self.__pynk_img = []
        self.__clyde_img = []
        self.__blink_img =[]
        self.__inky_img = []
        self.__indefeso_img = []
        self.__pause_img = ""
        self.__pacman_morto = []
        self.__tangerina = ""

    @property
    def tangerina(self):
        return self.__tangerina

    @tangerina.setter
    def tangerina(self, value):
        self.__tangerina = value

    @property
    def pacman_morto(self):
        return self.__pacman_morto

    @pacman_morto.setter
    def pacman_morto(self, pacman_morto):
        self.__pacman_morto = pacman_morto

    @property
    def pause_img(self):
        return self.__pause_img

    @pause_img.setter
    def pause_img(self, pause_img):
        self.__pause_img = pause_img

    @property
    def indefeso_img(self):
        return self.__indefeso_img

    @indefeso_img.setter
    def indefeso_img(self, indefeso_img):
        self.__indefeso_img = indefeso_img

    @property
    def pynk_img(self):
        return self.__pynk_img

    @pynk_img.setter
    def pynk_img(self, pynk_img):
        self.__pynk_img = pynk_img

    @property
    def clyde_img(self):
        return self.__clyde_img

    @clyde_img.setter
    def clyde_img(self, clyde_img):
        self.__clyde_img = clyde_img

    @property
    def blink_img(self):
        return self.__blink_img

    @blink_img.setter
    def blink_img(self, blink_img):
        self.__blink_img = blink_img

    @property
    def inky_img(self):
        return self.__inky_img

    @inky_img.setter
    def inky_img(self, inky_img):
        self.__inky_img = inky_img

    @property
    def diretorio_atual(self):
        return self.__diretorio_atual

    @diretorio_atual.setter
    def diretorio_atual(self, diretorio_atual):
        self.__diretorio_atual = diretorio_atual

    @property
    def jogador_img(self):
        return self.__jogador_img

    @jogador_img.setter
    def jogador_img(self, jogador_img):
        self.__jogador_img = jogador_img

    @property
    def start_logo(self):
        return self.__start_logo

    @start_logo.setter
    def start_logo(self, logo):
        self.__start_logo = logo 

    def carregar_imagens(self) -> None: #de start 
        diretorio_imagem = os.path.join(self.diretorio_atual, 'sprites')
        self.start_logo = os.path.join(diretorio_imagem, 'logo1.png')
        self.start_logo = pygame.image.load(self.start_logo).convert()

        #imagens de pacman

        diretorio_imagens = os.path.join(self.diretorio_atual, 'sprites/pacman_imgs')
        for i in range(0,17):
            try:
                imagem = os.path.join(diretorio_imagens, f'{i}.png')
                self.pacman_morto.append(pygame.transform.scale(pygame.image.load(imagem).convert(), (30,30)))
            except pygame.error as e: 
                print(f'Erro ao carregar imagem {i}: {e}')
        for i in range (2,8):
            try:
                imagem = os.path.join(diretorio_imagens, f'{i}.png')
                self.jogador_img.append(pygame.transform.scale(pygame.image.load(imagem).convert(), (30,30)))
            except pygame.error as e: 
                print(f'Erro ao carregar imagem {i}: {e}')
        #imagens dos fantasmas:

        diretorio_inky = os.path.join(self.diretorio_atual, 'sprites/inky')
        diretorio_blink = os.path.join(self.diretorio_atual, 'sprites/blink')
        diretorio_clyde = os.path.join(self.diretorio_atual, 'sprites/clyde')
        diretorio_pynk = os.path.join(self.diretorio_atual, 'sprites/pynk')
        diretorio_indefeso = os.path.join(self.diretorio_atual, 'sprites/indefeso')

        for i in range(0,2):
            try:
                imagem_indefeso = os.path.join(diretorio_indefeso, f'{i}.png')
                self.indefeso_img.append(pygame.transform.scale(pygame.image.load(imagem_indefeso).convert(), (25,25)))

                imagem_inky = os.path.join(diretorio_inky, f'{i}.png')
                self.inky_img.append(pygame.transform.scale(pygame.image.load(imagem_inky).convert(), (25,25)))

                imagem_blink = os.path.join(diretorio_blink, f'{i}.png')
                self.blink_img.append(pygame.transform.scale(pygame.image.load(imagem_blink).convert(), (25,25)))

                imagem_clyde = os.path.join(diretorio_clyde, f'{i}.png')
                self.clyde_img.append(pygame.transform.scale(pygame.image.load(imagem_clyde).convert(), (25,25)))

                imagem_pynk = os.path.join(diretorio_pynk, f'{i}.png')
                self.pynk_img.append(pygame.transform.scale(pygame.image.load(imagem_pynk).convert(), (25,25)))
                
            except pygame.error as e: 
                print(f'Erro ao carregar imagem {i}: {e}')

        #imagem das telas de configurações (pause e áudio)

        diretorio_imagem = os.path.join(self.diretorio_atual, 'sprites') 
        self.pause_img = os.path.join(diretorio_imagem, 'pause.png')
        self.pause_img = pygame.image.load(self.pause_img).convert()

        #imagem da tangerina

        self.tangerina = os.path.join(diretorio_imagem, 'tangerina.png')
        self.tangerina = pygame.image.load(self.tangerina).convert()