from __future__ import annotations
from game.params import Cities, Diseases
from typing import Set

class Node:
    def __init__(self, name: Cities, disease: Diseases ):
        self.Connections: Set[Node] = set()

    def add_connection(self, node: Node):
        self.Connections.add(node)
        node.Connections.add(node)

    def remove_connection(self, node: Node):
        self.Connections.remove(node)
        node.Connections.remove(node)