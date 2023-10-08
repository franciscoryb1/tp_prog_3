from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GoRight:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Go Right

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", state=grid.start, cost=0, parent=None, action=None)

        # Initialize the reached dictionary with the initial state
        reached = {}
        reached[node.state] = True

        # Return if the node contains a goal state
        if node.state == grid.end:
            return Solution(node, reached)

        # Initialize the frontier with the initial node
        # In this example, the frontier is a queue
        frontier = QueueFrontier()
        frontier.add(node)

        while True:

            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(reached)

            # Remove a node from the frontier
            node = frontier.remove()

            # Go right
            successors = grid.get_neighbours(node.state)
            if 'right' in successors:

                # Get the successor
                new_state = successors['right']

                # Check if the successor is not reached
                if new_state not in reached:

                    # Initialize the son node
                    new_node = Node("", new_state,
                                    node.cost + grid.get_cost(new_state),
                                    parent=node, action='right')

                    # Mark the successor as reached
                    reached[new_state] = True

                    # Return if the node contains a goal state
                    # In this example, the goal test is run
                    # before adding a new node to the frontier
                    if new_state == grid.end:
                        return Solution(new_node, reached)

                    # Add the new node to the frontier
                    frontier.add(new_node)
