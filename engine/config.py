DEFAULT_FPS_INTERVAL = 60

class Config:
  fps: int
  window_width: int
  window_height: int

  def __init__(
    self,
    fps: int,
    window_width: int,
    window_height
  ):
    self.fps = fps
    self.window_width = window_width
    self.window_height = window_height
