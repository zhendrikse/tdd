from dataclasses import dataclass

@dataclass
class Country:
    name: str
    capital: str
    region: str
    subregion: str
    population: int
    cca3: str
    cca2: str
    ccn3: str
    unMember: bool
  
    @classmethod
    def from_json(cls, country_json):
      return Country(
          country_json.get("name").get("common"),
          country_json.get("capital"),
          country_json.get("region"),
          country_json.get("subregion"),
          country_json.get("population"),
          country_json.get("cca3"),
          country_json.get("cca2"),
          country_json.get("ccn3"),
          country_json.get("unMember"))

    def __eq__(self, other):
        assert isinstance(other, Country)
        return self.ccn3 == other.ccn3

    def __lt__(self, other):
        assert isinstance(other, Country)
        return self.ccn3 < other.ccn3

    def __hash__(self):
        return int(self.ccn3)

    def __str__(self):
        return "<{} | {}>".format(self.name, self.cca3)

    def __repr__(self):
        return "<{} | {}>".format(self.name, self.cca3)