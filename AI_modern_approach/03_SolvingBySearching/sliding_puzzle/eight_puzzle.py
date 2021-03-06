import numpy as np
from pprint import pprint

UP    = [ 1,  0]
DOWN  = [-1,  0]
LEFT  = [ 0,  1]
RIGHT = [ 0, -1]
GOAL = [[1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]]

def make_random_board(dim=3):
    tiles = list(range(dim * dim))
    np.random.shuffle(tiles)
    return [tiles[(i*dim):(i*dim + dim)] for i in range(dim)]


def get_gap(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return [i, j]

            
def print_board(board):
    print('[%s,\n %s\n %s]' % (board[0], board[1], board[2]))
    
            
def move(board, direction):
    assert direction in [UP, DOWN, LEFT, RIGHT]
    try:
        gap_position = get_gap(board)
        swap_position = [gap_position[0] + direction[0],
                         gap_position[1] + direction[1]]
        swap_value = board[swap_position[0]][swap_position[1]]
        board[gap_position[0]][gap_position[1]] = swap_value
        board[swap_position[0]][swap_position[1]] = 0
    except IndexError:
        print('Cannot move that direction')
    return board

        
def get_all_successive_states(board):
    successive_states = []
    for direction in [UP, DOWN, LEFT, RIGHT]:
        temp_board = np.copy(board)
        new_state = move(temp_board, direction)
        successive_states.append(new_state)
    return successive_states



            

def main():
    initial_state = make_random_board()
    unexplored_states = [initial_state]
    explored_states = []
    iteration = 1
    
    while GOAL not in unexplored_states:
        print('iteration:', iteration)
        next_state = unexplored_states.pop()
        successive_states = get_all_successive_states(next_state)
        for state in successive_states:
            print_board(state)
            if state not in unexplored_states:
                unexplored_states.append(state)
        explored_states.append(next_state)

        print('Explored:')
        for board in explored:
            print_board(board)
        print('Unexplored:')
        for board in unexplored:
            print_board(board)
    
main()
