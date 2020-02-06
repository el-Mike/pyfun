from engine.typings.pygame_surface import PygameSurface
from engine.game_object.game_object import GameObject

class Bird(GameObject):
  x: int
  y: int
  img: any

  def __init__(self, x: int, y: int, img: any):
    self.x = x
    self.y = y
    self.img = img

  def render(self, surface: PygameSurface) -> None:
    surface.blit(self.img, (self.x, self.y))    

  def update(self):
    print('BIRD UPDATED')
