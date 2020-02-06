from typing import Dict, List, NamedTuple, Callable

import os
import pygame

class SpriteConfig(NamedTuple):
  name: str
  path: str
  transforms: List[Callable]

class SpriteManager:
  _sprites: Dict[str, any]

  def __init__(self: 'SpriteManager') -> 'SpriteManager':
    self._sprites = dict()

  # sprinte_config tuple contains: name, path and transform functions
  # in the given order.
  def register(
    self: 'SpriteManager',
    sprite_configs: List[SpriteConfig]
  ) -> None:
    for sprite_config in sprite_configs:
      sprite = pygame.image.load(sprite_config.path)

      # apply transforms for given sprite.
      for transform in sprite_config.transforms:
        sprite = transform(sprite)

      # add new sprite to the sprites dictionary.
      self._sprites.update([(
        sprite_config.name,
        sprite
      )])

  def get(self: 'SpriteManager', key: str) -> any:
    return self._sprites.get(key)
