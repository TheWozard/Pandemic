from game.node import Node
from game.params import Cities
from typing import Dict

class Game:
    def __init__(self, board: Dict[Cities, Node]):
        self.Board = board