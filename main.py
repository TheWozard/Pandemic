from game.core import GameManger
from game.params import Cities, Diseases, CitiesInPlay, DiseasesInPlay, MaxOutbreaks, MaxCubes, InfectionRate, CitiesConnections, CitiesDiseases

def create_game():
    manager = GameManger(CitiesInPlay, DiseasesInPlay, CitiesConnections, CitiesDiseases, MaxOutbreaks, InfectionRate, MaxCubes)
    manager.validate_board_info()
    print(manager.start_new_game().Board)


if __name__ == "__main__": 
    create_game()