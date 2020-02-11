import rx
from rx import operators as ops

import pygame

from engine.config import Config

from engine.loop import Loop
from engine.window import Window
from engine.sprite_manager import SpriteManager
from engine.state import State

class Game:
  config: Config
  window: Window
  sprite_manager: SpriteManager
  state: State
  loop: Loop

  def __init__(self, config: Config):
    self.config = config
    self.window = Window(self.config)
    self.sprite_manager = SpriteManager()
    self.state = State()

  def step(self) -> None:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.loop.stop()
        pygame.quit()
        quit()

    self.window.render(self.state.getRenderables())

  def stop(self) -> None:
    self.loop.stop()


  def start(self) -> None:
    self.loop = Loop(self.config.fps)

    self.window.start()
    
    frames = self.loop.start()

    frames.subscribe(
      on_next=lambda x: self.step(),
      on_completed=lambda x: print('COMPLETED!')
    )

    # keeps program executing, as loop is based on interval Observable
    input()
