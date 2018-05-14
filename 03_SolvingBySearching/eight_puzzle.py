from pprint import pprint

UP    = [ 1,  0]
DOWN  = [-1,  0]
LEFT  = [ 0,  1]
RIGHT = [ 0, -1]

class Board():
    def __init__(self):
        self.state = [[1, 2, 3],
                      [4, 0, 5],
                      [6, 7, 9]]
        self.gap = self._get_gap()

    def __str__(self):
        return ('[%s,\n %s\n %s]\n'
                % (self.state[0], self.state[1], self.state[2]))

    def _get_gap(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return [i, j]
                

    def move(self, direction):
        assert direction in [UP, DOWN, LEFT, RIGHT]
        try:
            gap_position = self._get_gap()
            swap_position = [gap_position[0] + direction[0],
                             gap_position[1] + direction[1]]
            swap_value = self.state[swap_position[0]][swap_position[1]]
            self.state[gap_position[0]][gap_position[1]] = swap_value
            self.state[swap_position[0]][swap_position[1]] = 0
        except KeyError:
            print('Cannot move that direction')


def main():
    board = Board()
    print(board)
    board.move(UP)
    print(board)
    board.move(LEFT)
    print(board)
    
main()
