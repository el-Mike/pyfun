import os
import time

import pygame

from engine.game import Game
from engine.config import Config
from engine.sprite_manager import SpriteConfig

from background import Background
from bird import Bird

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

  background = Background(game.sprite_manager.get('bg'))
  birds = [
    Bird(230, 350, game.sprite_manager.get('bird1')),
    Bird(130, 350, game.sprite_manager.get('bird1')),
  ]

  game.state.add([background] + birds)

  game.start()

if __name__ == "__main__":
  main()
