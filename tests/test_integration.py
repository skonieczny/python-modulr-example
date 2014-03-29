import unittest
from mock import Mock, patch
from awesome_game.application import run_application


class UnitsTest(unittest.TestCase):
    
    def test_run(self):
        with patch('awesome_game.game_core._print') as print_function:
            run_application(['game_core:run'])
        print_function.assert_any_call("Unit Dragon: {'can_fly': True, 'strength': 18}.")
