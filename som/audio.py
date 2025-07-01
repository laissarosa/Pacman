import pygame
import os

class Audio:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.__diretorio_audios = os.path.join(os.path.dirname(__file__), 'trilha')
        self.__inicio_audio = 0

    @property
    def inicio_audio(self):
        return self.__inicio_audio

    @inicio_audio.setter
    def inicio_audio(self, value):
        self.__inicio_audio = value

    @property
    def diretorio_audios(self):
        return self.__diretorio_audios

    @diretorio_audios.setter
    def diretorio_audios(self, diretorio_audios):
        self.__diretorio_audios = diretorio_audios

    '''def ajustar_sons(self, cena):
        volume = pygame.mixer.Channel(5).get_volume()

        ajustando_sons = True
        while ajustando_sons: 
            #self.relogio.tick(self.fps)
            cena.relogio.tick(cena.fps)
            cena.ver_novo_volume(volume)
            cena.tela.tela.fill((0,0,0))
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
                    
                    pygame.mixer.Channel(5).set_volume(volume)
                    pygame.mixer.Channel(1).set_volume(volume)
                    pygame.mixer.Channel(3).set_volume(volume)
                    pygame.mixer.Channel(4).set_volume(volume)
                    pygame.mixer.Channel(6).set_volume(volume)
                    pygame.mixer.Channel(7).set_volume(volume)
            
    def ajustar_musica(self, cena):
        volume = pygame.mixer.music.get_volume()

        ajustando_musica = True
        while ajustando_musica: 
            cena.relogio.tick(cena.fps)
            cena.ver_novo_volume(volume)
            cena.tela.tela.fill((0,0,0))
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
                    
                    pygame.mixer.music.set_volume(volume)
                    pygame.mixer.Channel(2).set_volume(volume)'''

    def ajustar_volume_sons(self, volume: float) -> None:
        pygame.mixer.Channel(5).set_volume(volume)
        pygame.mixer.Channel(1).set_volume(volume)
        pygame.mixer.Channel(3).set_volume(volume)
        pygame.mixer.Channel(4).set_volume(volume)
        pygame.mixer.Channel(6).set_volume(volume)
        pygame.mixer.Channel(7).set_volume(volume)

    def ajustar_volume_musica(self, volume: float) -> None:
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.Channel(2).set_volume(volume)

    def ouvir_tela_start (self):
        pygame.mixer.music.load(os.path.join(self.diretorio_audios, 'intermission.wav'))
        pygame.mixer.music.play(loops= -1)

    def parar_musica_start (self) -> None: 
        pygame.mixer.music.stop()
        som = pygame.mixer.Sound(os.path.join(self.diretorio_audios, 'credit.wav'))
        pygame.mixer.Channel(7).play(som)
        #pygame.mixer.sound = Create a new Sound object from a file or buffer object

    def ouvir_comer_bolinhas(self) -> None:
        som = pygame.mixer.Sound(os.path.join(self.diretorio_audios, 'eat_dot_0.wav'))
        pygame.mixer.Channel(1).play(som)

    def ouvir_superpoder (self) -> None:
            self.inicio_audio = pygame.time.get_ticks()
            som = pygame.mixer.Sound(os.path.join(self.diretorio_audios, 'fright.wav'))
            pygame.mixer.Channel(5).play(som ,loops=-1)
            pygame.mixer.Channel(2).pause()

    def parar_musica_superpoder (self) -> None:
        if self.inicio_audio != 0 and pygame.time.get_ticks() - self.inicio_audio >= 10000:
            pygame.mixer.Channel(5).stop()
            pygame.mixer.Channel(2).unpause()
            self.inicio_audio = 0
    
    def som_sirene (self, pacman_morto: bool) -> None: 
        if pacman_morto:
            pygame.mixer.Channel(2).stop()
        elif not pygame.mixer.Channel(2).get_busy():
            som = pygame.mixer.Sound(os.path.join(self.diretorio_audios, 'siren2.wav'))
            pygame.mixer.Channel(2).play(som,loops=-1)

    def parar_som_sirene (self):
        pygame.mixer.Channel(2).stop()
        
    def comer_fantasma(self):
        som = pygame.mixer.Sound(os.path.join(self.diretorio_audios, 'eat_ghost.wav'))
        pygame.mixer.Channel(3).play(som)  

    def morrer(self):
        pygame.mixer.Channel(2).stop()
        som = pygame.mixer.Sound(os.path.join(self.diretorio_audios, 'death_0.wav'))
        pygame.mixer.Channel(4).play(som) 

    def ouvir_comer_tangerina(self):
        som = pygame.mixer.Sound(os.path.join(self.diretorio_audios, 'eat_fruit.wav'))
        pygame.mixer.Channel(6).play(som)
    
                    
