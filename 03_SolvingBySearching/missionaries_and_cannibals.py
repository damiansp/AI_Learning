def get_boat_side(state):
    if state[0][2] == 1:
        return 0
    return 1

# Test
#print(get_boat_side([[0, 0, 0], [3, 3, 1]]))
#print(get_boat_side([[3, 3, 1], [0, 0, 0]]))


def cross_river(state, n_cannibals, n_missionaries, boat_side):
    new_state = [state[0][:], state[1][:]]
    change = [n_cannibals, n_missionaries, 1]
    for i, n in enumerate(change):
        new_state[boat_side][i] -= n
        new_state[1 - boat_side][i] += n
    return new_state

# Test
#state = [[3, 3, 1], [0, 0, 0]]
#print(cross_river(state, 1, 1, 0))
#print(cross_river(state, 2, 0, 0))
#state = [[1, 1, 0], [2, 2, 1]]
#print(cross_river(state, 2, 0, 1))


def is_legal(state):
    for bank in state:
        n_cannibals, n_missionaries = bank[0:2]
        if n_cannibals and n_missionaries and n_cannibals > n_missionaries:
            return False
    return True

# Test
#print(is_legal([[3, 3, 1], [0, 0, 0]]))
#print(is_legal([[3, 1, 0], [0, 2, 1]]))
    

def expand(state):
    boat_side = get_boat_side(state)
    cannibal_range = range(state[boat_side][0] + 1)
    missionary_range = range(state[boat_side][1] + 1)
    moves = [[c, m] for c in cannibal_range for m in missionary_range
             if 0 < c + m < 3]
    resulting_states = []
    for move in moves:
        c, m = move
        resulting_state = (cross_river(state, c, m, boat_side))
        if is_legal(resulting_state):
            resulting_states.append(resulting_state)
    return resulting_states

# Test
#print(expand([[3, 3, 1], [0, 0, 0]]))
#print(expand([[2, 2, 0], [1, 1, 1]]))

    
def main():
    goal_state = [[0, 0, 0], [3, 3, 1]]
    unexplored_states = [[[3, 3, 1], [0, 0, 0]]]
    explored_states =[]

    while goal_state not in explored_states:
        print('\nExplored States:')
        for es in explored_states:
            print(' ', es)
        next_state_to_explore = unexplored_states.pop()
        reachable_states = expand(next_state_to_explore)
        explored_states.append(next_state_to_explore)
        for state in reachable_states:
            if state not in explored_states:
                unexplored_states.append(state)

    print('Goal state found!')


main()
