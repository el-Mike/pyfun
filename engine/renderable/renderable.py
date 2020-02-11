from abc import ABC, abstractmethod

from engine.typings.pygame_surface import PygameSurface

class Renderable(ABC):
  @abstractmethod
  def render(self, surface: PygameSurface) -> None:
    pass
