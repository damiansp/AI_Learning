# The Missionaries and Cannibals Problem
# 3 missionaries and 3 cannibals are on one side of a river. Get all 6 to the
# other side of the river with the following constraints:
#   Only 2 people fit in the boat
#   Cannibals cannot outnumber missionaries on either bank

boat = 0 # 0: left side; 1: right side
world = [['c', 'c', 'c', 'm', 'm', 'm'], []]
goal = [[], ['c', 'c', 'c', 'm', 'm', 'm']]
fringe = [world]
visted_states = [world]
actions = [['c'], ['c','c'], ['c', 'm'], ['m'], ['m', 'm']]

def is_valid_state(state):
    for shore in [0, 1]:
        if 'm' in state[shore]:
            n_m = 0
            n_c = 0
            for person in state[shore]:
                if person == 'm':
                    n_m += 1
                else:
                    n_c += 1
            if n_c > n_m:
                return False
    return True

# Test
#print is_valid_state(world)
#print is_valid_state([['c', 'c', 'c'],['m', 'm', 'm']])
#print is_valid_state([['c', 'm', 'm', 'c'], ['c', 'm']])
#print is_valid_state([['c', 'm', 'c'], ['c', 'm', 'm']])


def act(action):
    global world
    current_state = list(world)
    c_to_cross = 0
    m_to_cross = 0
    c_on_land = 0
    m_on_land = 0

    for person in current_state[boat]:
        if person == 'c':
            c_on_land += 1
        else:
            m_on_land += 1

    for person in action:
        if person == 'c':
            c_to_cross += 1
        else:
            m_to_cross += 1

    print ('C crossing:', c_to_cross, 'M crossing:', m_to_cross, 'C on land:',
           c_on_land, 'M on land:', m_on_land)
    # Check for invalid moves b/c required people not present
    if (c_to_cross > c_on_land) or (m_to_cross > m_on_land):
        return None

    # Cross the river
    for missionary in range(m_to_cross):
        # For all arrays, c's come first, m's at the end:
        current_state[boat] = current_state[boat][:-1]
        current_state[1 - boat] += ['m']
    for cannibal in range(c_to_cross):
        current_state[boat] = current_state[boat][1:]
        current_state[1 - boat] = ['c'] + current_state[1 - boat]

    if is_valid_state(current_state):
        return current_state
    else:
        return None


# Test
#for action in actions:
#    print 'Action:',  action, '\nResult:', act(action), '\n'

