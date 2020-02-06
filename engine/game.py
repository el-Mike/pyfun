import pygame
import rx
from rx import operators as ops

from engine.config import Config

from engine.loop import Loop
from engine.window import Window
from engine.sprite_manager import SpriteManager

class Game:
  config: Config
  window: Window
  sprite_manager: SpriteManager

  def __init__(self: 'Game', config: Config) -> 'Game':
    self.config = config
    self.window = Window(self.config)
    self.sprite_manager = SpriteManager()

  def step(self: 'Game') -> None:
    bg = self.sprite_manager.get('bg')
    
    self.window.surface.blit(bg, (0, 0))

    pygame.display.update()

  def start(
    self: 'Game',
  ) -> None:
    loop = Loop(self.config.fps)

    self.window.start()
    
    frames = loop.start()

    frames.subscribe(lambda v: self.step())

    # keeps program executing, as loop is based on interval Observable
    input()
