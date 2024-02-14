import pytest

from hamcrest import is_, assert_that

from src.coordinates import Coordinates
from src.pellet_group import PelletGroup
from src.ports.screen import Screen
from src.sprites.pellet import Pellet, PELLET_RADIUS, POWER_PELLET_RADIUS
from .adapters.fake_screen import FakeScreen
from .screen_observer import FakeScreenObserver


class TestRenderPelletGroup:
    _screen_observer = None

    @pytest.fixture(autouse=True)
    def screen_observer(self):
        self._screen_observer = FakeScreenObserver()

    @pytest.fixture
    def screen(self) -> Screen:
        return FakeScreen(self._screen_observer)

    def test_render_single_pellet(self, screen):
        pellet = Pellet(Coordinates(100, 110))
        pellet.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PELLET_RADIUS} rendered at <100, 110>'))

    def test_render_single_power_pellet(self, screen):
        pellet = Pellet(Coordinates(100, 110), is_power_pellet=True)
        pellet.render(screen)
        assert_that(len(self._screen_observer.messages), is_(1))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {POWER_PELLET_RADIUS} rendered at <100, 110>'))

    def test_render_pellet_group(self, screen):
        pellets = [Pellet(Coordinates(100, 110)),
                   Pellet(Coordinates(100, 120), is_power_pellet=True)]
        pellet_group = PelletGroup(pellets)
        pellet_group.render(screen)
        assert_that(len(self._screen_observer.messages), is_(2))
        assert_that(self._screen_observer.messages[0], is_(
            f'Circle with radius {PELLET_RADIUS} rendered at <100, 110>'))
        assert_that(self._screen_observer.messages[1], is_(
            f'Circle with radius {POWER_PELLET_RADIUS} rendered at <100, 120>'))
