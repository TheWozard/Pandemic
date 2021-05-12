from game.node import Node
from typing import Set, Dict, List
from game.params import Cities, Diseases
from game.game import Game

class GameManger:
    def __init__(self, cities: Set[Cities], diseases: Set[Diseases], connections: Dict[Cities, Set[Cities]], infections: Dict[Cities, Diseases], outbreaks: int, infectionRate: List[int], maxInfections: Dict[Diseases, int]):
        self.Cities = cities
        self.Diseases = diseases
        self.Connections = connections
        self.Infections = infections
        self.Outbreaks = outbreaks
        self.InfectionRate = infectionRate
        self.MaxInfections = maxInfections

    def start_new_game(self) -> Game:
        nodes = {}
        for city in self.Cities:
            node = Node(city, self.Infections[city])
            connection = self.Connections[city]
            for link in connection:
                if link in nodes:
                    target = nodes[link]
                    node.add_connection(target)
            nodes[city] = node
        return Game(nodes)


    def validate_board_info(self):
        for city in self.Cities:
            connection = self.Connections[city]
            for link in connection:
                if city not in self.Connections[link]:
                    print(f'{link} is not connected back to {city}')
            if city in connection:
                print(f'{city} cannot be linked to itself')
            disease = self.Infections[city]
            if disease not in self.Diseases:
                print(f'{disease} is not a valid disease')
