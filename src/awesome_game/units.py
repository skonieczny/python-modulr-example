from modulr.application import Component, simple_component_factory


def units_factory(game_core):
    
    class Units(Component):
        
        def __init__(self):
            game_core.register_unit('Peasant', strength=1, can_build=True)
            game_core.register_unit('Knight', strength=5)
            game_core.register_unit('Dragon', strength=18, can_fly=True)

    return Units()


units_component_factory = simple_component_factory(units_factory, [])
