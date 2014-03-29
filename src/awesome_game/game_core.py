from modulr.application import Component, simple_component_factory


def game_core_factory(context):
    
    class GameCore(Component):
        
        def __init__(self):
            self._units = {}
            context.scripts_manager.register('game_core:run', self.run_game_script)

        def get_units(self):
            return self._units

        def register_unit(self, name, **kwargs):
            self._units[name] = kwargs

        def run_game_script(self, args):
            self.run()
            
        def run(self):
            print 'Let\'s play with units: {}'.format(self._units)

    return GameCore()


game_core_component_factory = simple_component_factory(game_core_factory, ['game_core'])
