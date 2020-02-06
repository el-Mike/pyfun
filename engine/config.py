DEFAULT_FPS_INTERVAL = 60

class Config:
  fps: int

  def __init__(
    self: 'Config',
    fps: int
  ):
    self.fps = fps
