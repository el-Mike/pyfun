from abc import abstractmethod

from engine.renderable.renderable import Renderable

class GameObject(Renderable):
  @abstractmethod
  def update(self: 'GameObject') -> 'GameObject':
    pass
