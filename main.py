import json

from game.core import GameManger
from game.params import Cities, Diseases, CitiesInPlay, DiseasesInPlay, MaxOutbreaks, MaxCubes, InfectionRate, CitiesConnections, CitiesDiseases

def create_game_factory():
    manager = GameManger(CitiesInPlay, DiseasesInPlay, CitiesConnections, CitiesDiseases, MaxOutbreaks, InfectionRate, MaxCubes)
    manager.validate_board_info()
    return manager


if __name__ == "__main__": 
    factory = create_game_factory()
    game = factory.start_new_game()
    print(json.dumps(game.board_state(), indent=4))