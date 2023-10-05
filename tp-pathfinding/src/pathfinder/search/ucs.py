from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
# Initialize a node with the initial position
        node = Node("", state=grid.start, cost=0, parent=None, action=None)

        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)
        
        explored = {} 
        explored[node.state] = node.cost
        
        while True:

            if frontier.is_empty():
                return NoSolution(explored)

            node = frontier.pop()
            successors = grid.get_neighbours(node.state)
            cost= grid.get_cost(node.state)
            
            for action in successors: 
                
                new_state = successors[action]
                if new_state == grid.end:
                    return Solution(node, explored)
                
                new_cost = node.cost + cost
                
                if new_state not in explored or new_cost < explored[new_state]:
                    new_node = Node("", new_state, new_cost, parent=node, action=action)
                    
                    explored[new_state] = new_cost
                    
                    frontier.add(new_node ,new_cost)
