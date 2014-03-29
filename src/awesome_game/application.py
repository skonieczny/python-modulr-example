
from modulr.application import ConfiguredComponentFactory, Application,\
    ComponentFactoryRegistry
from awesome_game.units import units_component_factory
from awesome_game.game_core import game_core_component_factory
import sys

def get_app_config():
    # TODO: read from file
    return {}


def configure_components(component_factory_registry):
    # TODO: read from file or directory
    game_core_config = {}
    component_factory_registry.register(ConfiguredComponentFactory('game_core', game_core_component_factory, game_core_config))
    units_config = {}
    component_factory_registry.register(ConfiguredComponentFactory('units', units_component_factory, units_config))


def create_application():
    app_config = get_app_config()
    component_factory_registry = ComponentFactoryRegistry()
    configure_components(component_factory_registry)
    app = Application(app_config, component_factory_registry)
    app.start()
    return app


def run_application(arguments):
    app = create_application()
    app.get_scripts_manager().run_script_from_args(arguments)
    return app


if __name__ == "__main__":
    run_application(sys.argv[1:])
