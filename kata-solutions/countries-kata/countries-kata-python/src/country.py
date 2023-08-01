from dataclasses import dataclass

@dataclass
class Country:
  name: str
  capital: str
  population: int

  def as_string(self):
    return self.name + "," + self.capital + "," + str(self.population)
