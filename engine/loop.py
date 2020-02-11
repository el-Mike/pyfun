import rx
from rx import operators as ops

class Loop:
  _frames: rx.Observable
  _fps: int

  loop: rx.subject.Subject

  def __init__(self, fps: int):
    self._fps = fps

  def start(self) -> rx.Observable:
    self._frames = rx \
      .interval(1 / self._fps, scheduler=rx.scheduler.TimeoutScheduler()) \
      .pipe(
        ops.share(),
      )

    return self._frames

  def stop(self) -> None:
    self._frames.dispose()
