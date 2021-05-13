import json

from game.game_factory import GameFactory
from game.params import Cities

if __name__ == "__main__": 
    factory = GameFactory()
    game = factory.start_new_game()
    print(json.dumps(game.board_state(), indent=4))
