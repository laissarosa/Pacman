from personagens.fantasma import Fantasma

class Pynk(Fantasma):
<<<<<<< HEAD
=======

    """
    Classe que representa o fantasma Pynk, herdando o comportamento base
    da classe Fantasma.

    O Pynk possui uma inteligência de perseguição baseada na previsão do
    movimento do Pac-Man, definindo como alvo uma posição alguns blocos
    à frente da direção atual do jogador.

    Quando o Pac-Man está em estado poderoso, o Pynk muda seu comportamento
    para fuga. Caso contrário, ele utiliza estratégias de decisão para
    navegar pelo labirinto, tentando interceptar o Pac-Man de forma mais
    estratégica do que uma perseguição direta.
    """

>>>>>>> 8639339 (add code documentation)
    def __init__(self, imagem, velocidade = 1.3):
        super().__init__(imagem, velocidade)
        self.lista_imagens = self.imagem.pynk_img

<<<<<<< HEAD
    '''def  inicializar_posicao(self) -> None:
        self.x = 14 * 16
        self.y = 14 * 18'''

=======
>>>>>>> 8639339 (add code documentation)
    def mover(self,pacman_poderoso: bool, x_pac : int, y_pac: int, direcao_pac: int, tabuleiro: list, celula_largura: int, celula_altura: int) -> None:
        if not self.fantasma_saiu :
            self.x , self.y = self.sair_da_casinha(256, 216,tabuleiro, celula_largura, celula_altura)
            if round(self.y) == 216:
                self.fantasma_saiu = True
            return 

        if pacman_poderoso:
           self.x, self.y , self.direcao =  self.fugir( self.direcao, x_pac, y_pac, tabuleiro, celula_largura, celula_altura)
           return
        else:
            
            deslocamento_x = 5 * celula_largura
            deslocamento_y = 5 * celula_altura 
            alvo_pacman = (x_pac, y_pac) 

            if direcao_pac == 0:
                alvo_pacman = (x_pac + deslocamento_x, y_pac)
            elif direcao_pac == 1:
                alvo_pacman = (x_pac - deslocamento_x, y_pac)
            elif direcao_pac == 2:
                alvo_pacman = (x_pac, y_pac - deslocamento_y)
            elif direcao_pac == 3:
                alvo_pacman = (x_pac, y_pac + deslocamento_y)

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