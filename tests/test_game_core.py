import unittest
from mock import sentinel, Mock
from modulr.scripts import ScriptsManager
from awesome_game.game_core import game_core_factory


class GameCoreTest(unittest.TestCase):
    
    def _create_component(self):
        self._scripts_manager = ScriptsManager()
        context = Mock(scripts_manager=self._scripts_manager)
        game_core = game_core_factory(context)
        return game_core

    def test_registers_script_that_runs_run_method(self):
        game_core = self._create_component()
        game_core.run = Mock(wraps=game_core.run)
        self._scripts_manager.run_script('game_core:run', sentinel.args)
        game_core.run.assert_called_once_with()

    def test_register_unit(self):
        game_core = self._create_component()
        self.assertEqual(game_core.get_units(), {})
        game_core.register_unit('unit_name', property_name='property_value')
        self.assertEqual(game_core.get_units(), {'unit_name': {'property_name': 'property_value'}})
        