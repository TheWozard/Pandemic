from game.node import Node
from typing import Set, Dict, List
from game.params import Cities, CitiesConnections, CitiesDiseases, CitiesInPlay, Diseases, DiseasesInPlay, InfectionRate, MaxCubes, MaxOutbreaks
from game.game import Game


class GameFactory:
    def __init__(self):
        self.cities = CitiesInPlay
        self.diseases = DiseasesInPlay
        self.connections = CitiesConnections
        self.infections = CitiesDiseases
        self.outbreaks = MaxOutbreaks
        self.infection_rate = InfectionRate[:5]
        self.max_infections = MaxCubes
        self.starting_city = Cities.Atlanta

    def start_new_game(self) -> Game:
        nodes = {}
        for city in self.cities:
            node = Node(city, self.infections[city])
            connection = self.connections[city]
            for link in connection:
                if link in nodes:
                    target = nodes[link]
                    node.add_connection(target)
            nodes[city] = node
        return Game(nodes, self.diseases, [*self.infection_rate], self.starting_city)
