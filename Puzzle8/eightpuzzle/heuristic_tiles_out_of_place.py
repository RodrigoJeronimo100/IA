
from agents.heuristic import Heuristic
from eightpuzzle.eight_puzzle_state import EightPuzzleState


class HeuristicTilesOutOfPlace(Heuristic):

    def __init__(self):
        super().__init__()

    # TODO
    def compute(self, state: EightPuzzleState) -> float:
        h = 0
        for i in range(state.rows):
            for j in range(state.columns):
                tile = state.tiles[i][j]
                #Blank is ignored so that the heuristic is admissible.
                if tile != 0:
                   tile_goal = self._problem.goal_state.matrix[i][j]
                   if tile != tile_goal:
                       h += 1

        return h

    def __str__(self):
        return "Tiles out of place"
