import time

from engine.game import Game
from engine.config import Config

def main():
  config = Config(60)

  game = Game(config)

  game.start()

if __name__ == "__main__":
  main()
