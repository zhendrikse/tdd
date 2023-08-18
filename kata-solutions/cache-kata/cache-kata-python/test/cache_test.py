from typing import Protocol
import pytest
from hamcrest import assert_that, equal_to

from cache import Cache

CONTENTS_BEFORE_REFRESH = ["aap", "noot", "mies"]
CONTENTS_AFTER_REFRESH = ["jan", "piet", "klaas"]

class ContentsRepository(Protocol):
  def load(self):
    pass

class CLock(Protocol):
  def current_time_in_seconds(self):
    pass
    
class FakeClock:
  def __init__(self):
    self._current_time = 0
    
  def advance_sixty_seconds(self):
    self._current_time += 60

  def current_time_in_seconds(self):
    return self._current_time

class InMemoryRepository:
  def __init__(self):
    self._calls_to_load_method_counter = 0
    
  def load(self):
    if self._calls_to_load_method_counter == 0:
      contents = CONTENTS_BEFORE_REFRESH
    else:
      contents = CONTENTS_AFTER_REFRESH
    self._calls_to_load_method_counter += 1
    return contents 


class TestCache:  
  @pytest.fixture(autouse=True)
  def a_new_cache(self):
    return Cache(repository = InMemoryRepository(), clock = FakeClock())
    
  def test_initial_cache_is_empty(self, a_new_cache):
    assert_that(a_new_cache.is_empty(), equal_to(True))

  def test_request_contents_from_cache(self, a_new_cache):
    assert_that(a_new_cache.get_contents(), equal_to(CONTENTS_BEFORE_REFRESH))

  def test_request_same_contents_from_cache_twice(self, a_new_cache):
    _ = a_new_cache.get_contents()
    assert_that(a_new_cache.get_contents(), equal_to(CONTENTS_BEFORE_REFRESH))

  def test_request_updated_contents_from_cache_after_expiration(self, a_new_cache):
    _ = a_new_cache.get_contents()
    a_new_cache._clock.advance_sixty_seconds()    
    assert_that(a_new_cache.get_contents(), equal_to(CONTENTS_AFTER_REFRESH))
