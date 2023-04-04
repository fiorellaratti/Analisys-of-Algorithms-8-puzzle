
from queue import Queue

def Depth_First_Search(initial, goal):
    moves = ['up', 'down', 'left', 'right']

    initial = tuple(initial)
    goal = tuple(goal)

    visited = set()
    stack = [(initial, 0)]

    while stack:
        curr_state, cost = stack.pop()

        if curr_state == goal:
            return cost

        visited.add(curr_state)

        zero_index = curr_state.index(0)

        zero_row, zero_col = divmod(zero_index, 3)

        for move in moves:
            if move == 'up':
                new_row = zero_row - 1
                new_col = zero_col
            elif move == 'down':
                new_row = zero_row + 1
                new_col = zero_col
            elif move == 'left':
                new_row = zero_row
                new_col = zero_col - 1
            elif move == 'right':
                new_row = zero_row
                new_col = zero_col + 1

            if 0 <= new_row < 3:
                if 0 <= new_col < 3:
                    new_index = new_row * 3 + new_col

                    new_state = list(curr_state)
                    new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                    new_state = tuple(new_state)

                    if new_state not in visited:
                        stack.append((new_state, cost + 1))
        moves.reverse()

    return "Unsolvable"
