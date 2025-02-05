from .movie import Movie


class ChildrensMovie(Movie):
    def __init__(self, title):
        super().__init__(title)

    def calculate_amount(self, days_rented):
        amount = 1.5
        if days_rented > 3:
            amount += (days_rented - 3) * 1.5
        return amount

    def calculate_frequent_renter_points(self, days_rented):
        return 1
