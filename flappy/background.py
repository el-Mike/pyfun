from engine.typings.pygame_surface import PygameSurface
from engine.renderable.renderable import Renderable


class Background(Renderable):
  x: int
  y: int
  img: any

  def __init__(self: 'Background', img: any):
    self.x = 0
    self.y = 0
    self.img = img

  def render(self: 'Background', surface: PygameSurface) -> None:
    surface.blit(self.img, (self.x, self.y))
