from typing import List

from engine.renderable.renderable import Renderable
from engine.game_object.game_object import GameObject

class State:
  entities: List[Renderable]

  def __init__(self: 'State') -> 'State':
    self.entities = []

  def add(self: 'State', renderables: List[Renderable]) -> None:
    for renderable in renderables:
      self.entities.append(renderable)

  def getRenderables(self: 'State') -> List[Renderable]:
    return self.entities

  def getGameObjects(self: 'State') -> List[GameObject]:
    return filter(lambda g: isinstance(g, GameObject), self.entities)
