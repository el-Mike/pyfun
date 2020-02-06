from typing import Dict, List

import os
import pygame

class SpriteManager:
  _sprites: Dict

  def __init__(self: 'SpriteManager') -> 'SpriteManager':
    self._sprites = dict()

  def register(
    self: 'SpriteManager',
    name: str,
    path: str,
    transform_functions: List = []
  ) -> None:
    print('registering' + path)
    sprite = pygame.image.load(path)

    print(sprite)

    # apply transforms for given sprite.
    for transform_fn in transform_functions:
      transform_fn(sprite)

    # add new sprite to the sprites dictionary.
    self._sprites.update([(name, sprite)])

  def get(self: 'SpriteManager', key: str) -> any:
    return self._sprites.get(key)
