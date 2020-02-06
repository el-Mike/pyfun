import pygame
import rx
from rx import operators as ops

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

  def __init__(self: 'Game', config: Config) -> 'Game':
    self.config = config
    self.window = Window(self.config)
    self.sprite_manager = SpriteManager()
    self.state = State()

  def step(self: 'Game') -> None:    
    self.window.render(self.state.getRenderables())


  def start(
    self: 'Game',
  ) -> None:
    loop = Loop(self.config.fps)

    self.window.start()
    
    frames = loop.start()

    frames.subscribe(lambda v: self.step())

    # keeps program executing, as loop is based on interval Observable
    input()
