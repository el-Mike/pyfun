import rx
from rx import operators as ops

from .config import Config

from .loop import Loop

class Game:
  config: Config

  def __init__(self: 'Game', config: Config):
    self.config = config

  def start(
    self: 'Game',
  ) -> None:
    loop = Loop(self.config.fps)
    
    frames = loop.start()

    frames.subscribe(lambda value: print(value))

    # keeps program executing, as loop is based on interval Observable
    input()
