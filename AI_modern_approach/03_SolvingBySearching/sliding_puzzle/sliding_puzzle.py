# NEXT: Pick off unxeplored states 
import numpy as np


def main():
    game = Game(3)
    next_states = game._generate_moves(game.unexplored_states[0])
    for state in next_states:
        print(state)


class Game:
    def __init__(self, dim):
        self.board = Board(3)
        print('Starting a new game with board initialized as:')
        print(self.board)
        self.unexplored_states = [self.board.state.copy()]
        self.explored_states = []

    def _generate_moves(self, state):
        new_states = []
        for direction in self.board.MOVES:
            try:
                self.board.state = state.copy()
                self.board.move(direction)
                new_states.append(self.board.state.copy())
            except ValueError as e:
                #print(e)
                continue
        return new_states
                
                

class Board:
    MOVES = {'UP':    np.array([ 1,  0]),
             'DOWN':  np.array([-1,  0]),
             'LEFT':  np.array([ 0,  1]),
             'RIGHT': np.array([ 0, -1])}
    
    def __init__(self, dim=3):
        self.dim = dim
        self._state = self._get_random_board()
        self.goal = np.array(range(dim * dim)).reshape(self.dim, self.dim)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    
    def __str__(self):
        return repr(self.state)

    def _get_random_board(self):
        n_tiles = self.dim ** 2
        state = np.random.choice(range(n_tiles), n_tiles, replace=False)\
                         .reshape(self.dim, self.dim)
        return state

    def move(self, direction):
        d = self.MOVES[direction]
        zero_ind = np.where(self.state == 0)
        zero_ind = np.array([zero_ind[0][0], zero_ind[1][0]])
        swap_ind = zero_ind + d
        for i in swap_ind:
            if i < 0 or i >= self.dim:
                raise ValueError(f'{direction} not a legal move')
                return
        swap_val = self.state[swap_ind[0], swap_ind[1]]
        self.state[zero_ind[0], zero_ind[1]] = swap_val
        self.state[swap_ind[0], swap_ind[1]] = 0


if __name__ == '__main__':
    main()
