## 🟡 Pac-Man em Python

Recriação do clássico jogo Pac-Man em Python, desenvolvido para a disciplina de Orientação a Objetos. O projeto utiliza a biblioteca Pygame para implementação de gráficos, movimentação, colisões e interação com o jogador.

## 📂 Funcionalidades

- Movimentação do Pac-Man por setas do teclado
- Fantasmas com comportamento distinto
- Contagem de pontos e vidas
- Labirinto com paredes e caminhos delimitados
- Estrutura orientada a objetos para personagens e labirinto
- Salvamento e carregamento do progresso do jogo

## 🚀 Objetivo

- Aplicar conceitos de Orientação a Objetos em Python
- Desenvolver habilidades em programação de jogos com Pygame
- Praticar organização de código modular e reutilizável

## 🖥️ Tecnologias

- Linguagem: Python 3
- Biblioteca: Pygame

📁 Estrutura do Projeto

O projeto está organizado de forma modular, separando responsabilidades como personagens, recursos visuais, sons e lógica principal do jogo. Essa organização facilita a manutenção, leitura do código e futuras expansões.
```
📦 projeto-pacman
├── 📁 main
│   └── pacmain.py            # Arquivo principal responsável por iniciar o jogo
│
├── 📁 desenvolvimento
│   └── jogo.py               # Classe Jogo, responsável pelo loop principal e controle do jogo
│
├── 📁 personagens
│   ├── fantasma.py           # Classe base dos fantasmas
│   ├── clyde.py              # Fantasma Clyde (comportamento baseado em distância)
│   ├── inky.py               # Fantasma Inky (movimento semi-aleatório)
│   ├── pynk.py               # Fantasma Pynk (antecipação da posição do Pacman)
│   ├── pacman.py             # Classe principal do jogador
│   └── tangerina.py          # Item especial que concede bônus ao jogador
│
├── 📁 imagens
│   ├── imagem.py             # Gerenciamento e carregamento das imagens do jogo
│   └── 📁 sprites
│       ├── 📁 clyde          # Sprites do fantasma Clyde
│       ├── 📁 inky           # Sprites do fantasma Inky
│       ├── 📁 blink          # Sprites do fantasma Blink
│       ├── 📁 pynk           # Sprites do fantasma Pynk
│       ├── 📁 pacman_imgs    # Sprites e animações do Pacman
│       └── 📁 indefeso       # Sprites dos fantasmas em estado de medo
│
├── 📁 som
│   ├── audio.py              # Controle de efeitos sonoros e trilha sonora
│   └── 📁 trilha             # Arquivos de áudio (.wav) utilizados no jogo
│
└── 📄 README.md               # Documentação do projeto

```
## ⚠️ Observações

- Projeto com finalidade acadêmica
- Pode ser expandido ou modificado para fins de estudo e experimentação
