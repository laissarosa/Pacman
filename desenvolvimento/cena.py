import pygame
from pygame.locals import QUIT
import sys
import os
from som.audio import Audio
from imagens.imagem import Imagem
from pygame import Surface
#para controlar as telas start,game over e tudo+ que aparece na tela, como a tela de pause ou a tela de configurar audio
class Cena:
    def __init__(self, imagem: Imagem):
        pygame.init()
        self.__inicializar()
        self.__fonte = pygame.font.match_font('georgia')
        self.__relogio = self.__relogio = pygame.time.Clock()
        self.__fps = 60
        self.__imagem = imagem

    @property
    def imagem(self):
        return self.__imagem

    @imagem.setter
    def imagem(self, imagem):
        self.__imagem = imagem

    @property
    def relogio(self):
        return self.__relogio

    @relogio.setter
    def relogio(self, imagem):
        self.__relogio = imagem

    @property
    def fps(self):
        return self.__fps

    @fps.setter
    def fps(self, value):
        self.__fps = value

    @property
    def fonte(self):
        return self.__fonte

    @fonte.setter
    def fonte(self, fonte):
        self.__fonte = fonte

    def __inicializar(self) -> None:
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'imagens')))
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'audio')))
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    def mostrar_texto (self, texto: str, tamanho : int, cor: None, x: int, y:int, tela: Surface ) -> None:
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x,y)
        tela.blit(texto, texto_rect)

    def mostrar_tela_start (self, tela: Surface, audio: Audio) -> bool: #pergunatar se imagem e tela é bom de ter aqui
        audio.ouvir_tela_start()
        start_logo_rect = self.imagem.start_logo.get_rect()
        start_logo_rect.midtop = (250, 50)
        tela.blit(self.imagem.start_logo,start_logo_rect)
        self.mostrar_texto ('Pressione uma tecla para jogar', 23, (244,233,31), 250 , 320, tela)
        self.mostrar_texto ('Continuar de onde parou? Aperte S', 18, (244,233,31),250 , 370, tela)
        self.mostrar_texto ('Aperte M para configurar volume', 18, (244,233,31), 250 , 395, tela)
        self.mostrar_texto('Desenvolvido por Laissa Rosa-9390', 17, 'white',250, 520,tela)
        pygame.display.flip()
        return self.esperar_jogador(tela, audio)

    def esperar_jogador(self, tela: Surface, audio: Audio) -> bool:
        esperando = True
        while esperando: 
            self.relogio.tick(self.fps)
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    esperando = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        if os.path.exists("save.json"):
                            esperando = False
                            audio.parar_musica_start()
                            return True
                    elif event.key == pygame.K_m:
                        self.tela_configurar_volume(tela, audio)
                    esperando = False
                    audio.parar_musica_start()
                    return False

    def mostrar_pontuação(self, pontuacao: int, tela: Surface) -> None:  # posso fazer pontuaçõa e vidas juntas
         self.mostrar_texto(f'Pontos:{pontuacao}', 15, 'yellow', 250, 600, tela)

    def desenhar_tela_final (self, todas_bolinhas: int, vidas:int, tela: Surface, audio: Audio) -> bool:
        if todas_bolinhas == 0:
            self.mostrar_texto (f'VOCÊ GANHOU', 18, 'yellow', 240, 280, tela)
            self.mostrar_texto (f'Pressione R para reiniciar', 18, 'yellow', 250, 315, tela)
            audio.parar_som_sirene()
            return True
        if vidas ==  0: 
            self.mostrar_texto (f'GAME OVER', 18, 'yellow', 240, 280, tela)
            self.mostrar_texto('Pressione R para reiniciar', 20, 'yellow', 250, 315, tela)
            audio.parar_som_sirene()
            return True
            #jogo.fim_jogo = True
        return False
    
    def desenhar_configuracoes (self, tela: Surface) -> None:
        #self.imagem.carregar_img_pause()
        tela_pause = self.imagem.pause_img.get_rect()
        tela_pause.midtop = (250, 400)
        tela.blit(self.imagem.pause_img, tela_pause)
        self.mostrar_texto('Jogo Pausado: pressione P para continuar', 20, 'yellow', 250, 200, tela)
        self.mostrar_texto('Pressione R para reiniciar o jogo', 20, 'yellow', 250, 250, tela)
        self.mostrar_texto('Pressione S para salvar e sair', 20, 'yellow', 250,300, tela)

    def contar_vidas (self, vidas: int, tela: Surface): 
        for i in range (vidas):
            tela.blit(pygame.transform.scale(self.imagem.jogador_img[2], (20,20)), ((250 + 60) + i * 20 , 600))

    def ver_novo_volume(self, novo_volume: float, tela: Surface) -> None:
        tela.fill((0,0,0))
        #self.imagem.carregar_img_pause()
        tela_pause = self.imagem.pause_img.get_rect()
        tela_pause.midtop = (250, 400)
        tela.blit(self.imagem.pause_img, tela_pause)
        self.mostrar_texto(f'Volume: {int(novo_volume * 100)}%', 20, 'yellow', 250, 200, tela)
        self.mostrar_texto('Enter para sair', 15, 'yellow', 250, 230, tela)
        pygame.display.flip()

    def tela_configurar_volume(self, tela: Surface, audio: Audio) -> None:
        ajustando = True
        while ajustando:
            self.relogio.tick(self.fps)
            tela.fill((0,0,0)) 
            tela_pause = self.imagem.pause_img.get_rect()
            tela_pause.midtop = (250, 400)
            tela.blit(self.imagem.pause_img, tela_pause)
            self.mostrar_texto("Pressione 1 para alterar o volume dos sons de efeito", 20, 'yellow', 250, 200, tela)
            self.mostrar_texto('Pressione 2 para alterar o volume da musica do jogo', 20, 'yellow', 250, 250, tela)
            self.mostrar_texto('Pressione Enter para sair', 20, 'yellow', 250, 300, tela)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    ajustando = False #não posso ter isso aqui
                    #jogo.esta_rodando = False #fecho tudo se apertar para sair logo no início
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.ajustar_sons(tela, audio)
                        tela.fill((0, 0, 0))
                    elif event.key == pygame.K_2:
                        self.ajustar_musica(tela, audio)
                        tela.fill((0, 0, 0))
                    elif event.key == pygame.K_RETURN:
                        ajustando = False
            
    def ajustar_musica(self, tela: Surface, audio: Audio) -> None:
        volume = pygame.mixer.music.get_volume()

        ajustando_musica = True
        while ajustando_musica: 
            self.relogio.tick(self.fps)
            self.ver_novo_volume(volume, tela)
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    ajustando_musica = False
                   # jogo.esta_rodando = False #fecho tudo se apertar para sair logo no início
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        volume += 0.1
                    elif event.key == pygame.K_DOWN:
                        volume -= 0.1
                    elif event.key == pygame.K_RETURN:
                        ajustando_musica = False

                    volume = max(0.0, min(1.0, volume))
                    audio.ajustar_volume_musica(volume)
    
    def ajustar_sons(self, tela: Surface, audio: Audio) -> None:
        volume = pygame.mixer.Channel(5).get_volume()
        ajustando_sons = True
        while ajustando_sons: 
            #self.relogio.tick(self.fps)
            self.relogio.tick(self.fps)
            self.ver_novo_volume(volume, tela)
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    ajustando_sons = False
                    #jogo.esta_rodando = False #fecho tudo se apertar para sair logo no início
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        volume += 0.1
                    elif event.key == pygame.K_DOWN:
                        volume -= 0.1
                    elif event.key == pygame.K_RETURN:
                        ajustando_sons = False
                        
                    volume = max(0.0, min(1.0, volume))
                    audio.ajustar_volume_sons(volume)
                    
            