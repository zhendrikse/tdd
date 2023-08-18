
class Cache:
  def __init__(self, repository, clock, expiration_in_seconds = 60):
    self._repository = repository
    self._clock = clock
    self._last_time_updated = clock.current_time_in_seconds() - expiration_in_seconds
    self._contents = None
    self._expiration_in_seconds = expiration_in_seconds

  def _is_expired(self):
    return self._clock.current_time_in_seconds() - self._last_time_updated >= self._expiration_in_seconds
    
  def is_empty(self):
    return True

  def get_contents(self):
    if self._is_expired():
      self._contents = self._repository.load()
      self._last_time_updated = self._clock.current_time_in_seconds()
    return self._contents