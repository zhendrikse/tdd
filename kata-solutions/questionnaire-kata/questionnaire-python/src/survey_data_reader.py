from typing import Protocol

class SurveyDataReader(Protocol):
  def get_sheet_by_name(self, sheet_name):
      ...
