from abc import ABC, abstractmethod

from engine.typings.pygame_surface import PygameSurface

class GameObject(ABC):
  def update(self: 'GameObject') -> 'GameObject':
    pass

  def render(self: 'GameObject', surface: PygameSurface) -> None:
    pass
