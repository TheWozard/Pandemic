from __future__ import annotations
from game.params import Cities, Diseases
from typing import Dict, Set


class Node:
    def __init__(self, name: Cities, disease: Diseases):
        self._connections: Set[Node] = set()
        self._disease_type = disease
        self._disease_count = 0

    def add_connection(self, node: Node):
        self._connections.add(node)
        node._connections.add(node)

    def remove_connection(self, node: Node):
        self._connections.remove(node)
        node._connections.remove(node)

    def add_disease(self) -> int:
        if self._disease_count >= 3:
            sum = 1
            for node in self._connections:
                sum += node.add_disease()
            return sum
        self._disease_count += 1
        return 0

    def set_disease(self, count: int):
        self._disease_count = count

    def remove_disease(self):
        if self._disease_count <= 0:
            return
        self._disease_count -= 1

    def clear_disease(self):
        self._disease_count = 0

    def node_state(self) -> Dict[str, any]:
        return {
            "disease": self._disease_type.value,
            "count": self._disease_count,
        }
