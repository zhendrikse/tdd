from coordinates import Coordinates


class Screen:
    def __init__(self, resolution, framework, renderer, display):
        self._framework = framework
        self._renderer = renderer
        self._screen = display.set_mode((resolution.x, resolution.y))
        self._display = display
        framework.init()

    def render_circle(self, color: str, coordinates: Coordinates, radius: int) -> None:
        self._renderer.circle(self._screen, color, (coordinates.x, coordinates.y), radius)

    def flip(self) -> None:
        self._display.flip()

    def fill(self, color) -> None:
        self._screen.fill(color)

    def quit(self) -> None:
        self._framework.quit()

