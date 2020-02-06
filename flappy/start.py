import os
import time

from engine.game import Game
from engine.config import Config

FPS = 60
WIN_WIDTH = 500
WIN_HEIGHT = 800

local_dir = os.path.dirname(__file__)

def main():
  config = Config(
    FPS,
    WIN_WIDTH,
    WIN_HEIGHT
  )

  game = Game(config)

  game.sprite_manager.register(
    'bg',
    os.path.join(local_dir, "assets/bg.png")
  )

  game.start()

if __name__ == "__main__":
  main()
