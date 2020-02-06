import rx
from rx import operators as ops

class Loop:
  _frames: rx.Observable
  _fps: int

  def __init__(self: 'Loop', fps: int) -> 'Loop':
    self._fps = fps

  def start(self: 'Loop') -> rx.Observable:
    self._frames = rx \
      .interval(1 / self._fps, scheduler=rx.scheduler.TimeoutScheduler()) \
      .pipe(
        ops.share(),
      )

    return self._frames

