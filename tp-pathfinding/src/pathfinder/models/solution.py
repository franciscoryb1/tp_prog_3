from .node import Node

class Solution:
    """Model a solution to a pathfinding problem"""

    def __init__(
        self,
        node: Node,
        reached: dict[tuple[int, int], any],
        time: float = 0
    ) -> None:

        #  Generate path and return a Solution object
        path = []
        temp = node
        while temp.parent != None:
            path.append(temp.state)
            temp = temp.parent
        path.append(temp.state)
        path.reverse()

        self.path = path
        self.path_cost = node.cost
        self.path_length = len(path)
        self.explored = list(reached)
        self.explored_length = len(reached)
        self.time = time

    def __repr__(self) -> str:
        return (f"Solution([{self.path[0]}, ..., {self.path[-1]}],"
                f" {'{...}'}, {self.time})")


class NoSolution(Solution):
    """Model an empty pathfinding solution"""

    def __init__(
        self,
        reached: dict[tuple[int, int], any],
        time: float = 0
    ) -> None:
        self.path = []
        self.path_cost = 0
        self.path_length = 0
        self.explored = list(reached)
        self.explored_length = len(reached)
        self.time = time

    def __repr__(self) -> str:
        explored = list(self.explored)
        return (f"NoSolution([], {'{'}{explored[0]}, {explored[1]},"
                f" ...{'}'}, {self.time})")
