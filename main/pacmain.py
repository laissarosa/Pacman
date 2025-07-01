import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from desenvolvimento.jogo import Jogo

if __name__ == "__main__":
    jogo = Jogo() 
    jogo.rodar()

