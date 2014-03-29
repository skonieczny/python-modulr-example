import unittest
from mock import sentinel, Mock
from awesome_game.units import units_factory


class UnitsTest(unittest.TestCase):
    
    def _create_component(self, game_core):
        self._game_core = game_core
        units = units_factory(game_core)
        return units

    def test_registers_knight_unit(self):
        units = self._create_component(Mock())
        self._game_core.register_unit.assert_any_call('Knight', strength=5)
