import os
import time

import pygame

from engine.game import Game
from engine.config import Config
from engine.sprite_manager import SpriteConfig

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

  game.sprite_manager.register([
    SpriteConfig('bg', os.path.join(local_dir, "assets/bg.png"), [pygame.transform.scale2x]),
    SpriteConfig('bird1', os.path.join(local_dir, "assets/bird1.png"), [pygame.transform.scale2x]),
    SpriteConfig('bird2', os.path.join(local_dir, "assets/bird2.png"), [pygame.transform.scale2x]),
    SpriteConfig('bird3', os.path.join(local_dir, "assets/bird3.png"), [pygame.transform.scale2x]),
    SpriteConfig('base', os.path.join(local_dir, "assets/base.png"), [pygame.transform.scale2x]),
    SpriteConfig('pipe', os.path.join(local_dir, "assets/pipe.png"), [pygame.transform.scale2x]),
  ])

  game.start()

if __name__ == "__main__":
  main()
