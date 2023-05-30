class Game:
    def __init__(self, cells):
        self._cells = cells

    def next_generation(self):
        return Game(
            [self.next_row_generation(row) for row in range(self.height)])

    def next_row_generation(self, row):
        return [
            self.cell_at(row, i).next_generation(self.neighbours_for(row, i))
            for i in range(self.width)
        ]

    def neighbours_for(self, row, column):
        neighbours = [
            self.cell_at(row - 1, column - 1),
            self.cell_at(row - 1, column),
            self.cell_at(row - 1, column + 1),
            self.cell_at(row, column - 1),
            self.cell_at(row, column + 1),
            self.cell_at(row + 1, column - 1),
            self.cell_at(row + 1, column),
            self.cell_at(row + 1, column + 1),
        ]
        return without_nones(neighbours)

    def cell_at(self, row, column):
        if column < 0: return None
        if column >= self.width: return None
        if row < 0: return None
        if row >= self.height: return None
        return self._cells[row][column]

    @property
    def width(self):
        return len(self._cells[0])

    @property
    def height(self):
        return len(self._cells)

    def __str__(self):
        return '\n'.join([
            ''.join([cell.char_repr() for cell in row]) for row in self._cells
        ])


def without_nones(list):
    return [item for item in list if item is not None]


class Cell:
    def __init__(self, alive):
        self._alive = alive

    def next_generation(self, neighbours):
        if self.is_alive():
            return self._next_generation_when_alive(neighbours)

        return self._next_generation_when_dead(neighbours)

    def _next_generation_when_dead(self, neighbours):
        if len(living(neighbours)) == 3:
            return living_cell()
        return dead_cell()

    def _next_generation_when_alive(self, neighbours):
        if len(living(neighbours)) in [2, 3]:
            return living_cell()
        return dead_cell()

    def is_alive(self):
        return self._alive

    def __eq__(self, __o: object) -> bool:
        return self.is_alive() == __o.is_alive()

    def char_repr(self):
        return "#" if self.is_alive() else " "


def living(neighbours):
    return [neighbour for neighbour in neighbours if neighbour.is_alive()]


def dead_cell():
    return Cell(alive=False)


def living_cell():
    return Cell(alive=True)


from random import choice
import os, time

if __name__ == '__main__':
    game = Game([[choice([dead_cell, living_cell])() for c in range(80)]
                 for r in range(40)])
    while True:
        os.system('clear')
        print(game)
        game = game.next_generation()
        time.sleep(0.4)
