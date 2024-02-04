from .movie import Movie


class RegularMovie(Movie):
    def __init__(self, title):
        super().__init__(title)

    def calculate_amount(self, days_rented) -> int:
        amount = 2
        if days_rented > 2:
            amount += (days_rented - 2) * 1.5
        return amount

    def calculate_frequent_renter_points(self, days_rented) -> int:
        return 1
