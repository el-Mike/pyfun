from typing import List, cast

import pygame

from engine.typings.pygame_surface import PygameSurface

from engine.game_object.game_object import GameObject

from .config import Config

class Window:
  config: Config
  # pygame seems to be missing typings for a lot of it's modules
  surface: PygameSurface
  

  def __init__(self: 'Window', config: Config) -> 'Window':
    self.config = config

  def start(self: 'Window') -> PygameSurface:
    self.surface = cast(
      PygameSurface,
      pygame.display \
        .set_mode((self.config.window_width, self.config.window_height))
    )

    return self.surface

  def render(self: 'Window', game_objects: List[GameObject]) -> None:
    for game_object in game_objects:
      game_object.render(self.surface)

