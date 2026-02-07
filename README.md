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

📦 projeto-pacman
├── 📁 personagens
│   ├── fantasma.py        # Classe base dos fantasmas
│   ├── clyde.py           # Fantasma Clyde (comportamento baseado em distância)
│   ├── inky.py            # Fantasma Inky (movimento semi-aleatório)
│   ├── pynk.py            # Fantasma Pynk (antecipação da posição do Pacman)
│   ├── pacman.py          # Classe principal do jogador
│   └── tangerina.py       # Item especial que concede bônus ao jogador
│
├── 📁 imagens
│   └── imagem.py          # Gerenciamento e carregamento das imagens do jogo
│
├── 📁 som
│   ├── audio.py           # Controle de efeitos sonoros e trilha sonora
│   └── 📁 trilha          # Arquivos de áudio (.wav) utilizados no jogo
│
├── 📄 main.py              # Arquivo principal de execução do jogo
└── 📄 README.md            # Documentação do projeto


## ⚠️ Observações

- Projeto com finalidade acadêmica
- Pode ser expandido ou modificado para fins de estudo e experimentação
