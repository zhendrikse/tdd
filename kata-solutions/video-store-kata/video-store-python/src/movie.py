from enum import Enum
from dataclasses import dataclass

@dataclass(frozen = True)
class Movie:
  _title: str
	
  def get_title (self):
    return self._title
