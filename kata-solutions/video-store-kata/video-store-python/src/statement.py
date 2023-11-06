from regular_movie import RegularMovie
from new_release_movie import NewReleaseMovie
from childrens_movie import ChildrensMovie
from dataclasses import dataclass


@dataclass(frozen=True)
class StatementData:
    name: str
    amount_owed: float
    frequent_renter_points: int
    rental_amounts: []
    movie_titles: []


class Statement:
    def __init__(self, rentals, name):
        self._name = name
        self._rentals = rentals

    def calculate_amount(self):
        return sum(rental.calculate_amount() for rental in self._rentals)

    def calculate_frequent_renter_points(self) -> int:
        return sum(rental.calculate_frequent_renter_points() for rental in self._rentals)

    def export_data(self):
        return StatementData(
            name=self._name,
            amount_owed=self.calculate_amount(),
            frequent_renter_points=self.calculate_frequent_renter_points(),
            rental_amounts=[rental.calculate_amount() for rental in self._rentals],
            movie_titles=[rental.get_movie_title() for rental in self._rentals]
        )
