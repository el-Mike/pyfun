from typing import List, cast

import pygame

from engine.typings.pygame_surface import PygameSurface

from engine.renderable.renderable import Renderable

from .config import Config

class Window:
  config: Config
  # pygame seems to be missing typings for a lot of it's modules
  surface: PygameSurface
  

  def __init__(self, config: Config):
    self.config = config

  def start(self) -> PygameSurface:
    self.surface = cast(
      PygameSurface,
      pygame.display \
        .set_mode((self.config.window_width, self.config.window_height))
    )

    return self.surface

  def render(self, renderables: List[Renderable]) -> None:
    for renderable in renderables:
      renderable.render(self.surface)

    pygame.display.update()

