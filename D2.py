from queue import PriorityQueue


def print_current_state(state):
    for i in range(3):
        for j in range(3):
            print(state[i * 3 + j], end=" ")
        print()
    print()

def Dijkstra_Search(initial, goal):
    # possible moves
    moves = ['up', 'down', 'left', 'right'] 

    # Convert the goal state to a tuple for use as a key in sets and priority queues
    initial = tuple(initial)

    # convert the goal state to tuple and use the tuple as comparison key because tuple are immutable.
    goal = tuple(goal)

    # initialize a set to track the visited states and a priority queue to to store the unvisited ones
    is_visited = set()
    pq = PriorityQueue()

    # because values and cost are the same.
    pq.put((0, initial))

    while pq.empty != False:
        cost, current_state = pq.get()
        print(print_current_state(current_state))
        if current_state == goal:
            return cost

        is_visited.add(current_state)

        #find the index of the black tile
        blank_index = int()
        for i in range(len(current_state)):
            if current_state[i] == 0:
              blank_index = i
            
        blank_row, blank_col = divmod(blank_index, 3)  # 3 because is a 3x3 grid

        # For each possible move
        for move in moves:
            # Calculate the new row and column of the zero tile based on the move
            if move == 'left':
                new_row = blank_row
                new_col = blank_col - 1
            elif move == 'right':
                new_row = blank_row
                new_col = blank_col + 1
            elif move == 'up':
                new_row = blank_row - 1
                new_col = blank_col
            elif move == 'down':
                new_row = blank_row + 1
                new_col = blank_col
        
        print(move)
        
        if 0 <= new_row < 3:
            if 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = list(current_state)
                new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
                new_state = tuple(new_state)

                if new_state not in is_visited:
                    # calculate cost of moving to new state
                    move_cost = new_state[new_index]
                    cost = cost + move_cost

                    # add new state to priority queue with calculated cost
                    # because values and cost are the same.
                    pq.put((cost, new_state))
        print(new_index)
        moves.reverse()

    return "Unsolvable"


initial = [7, 2, 4,
           5, 0, 6,
           8, 3, 1]

goal1 = [1, 3, 4,
         8, 0, 2,
         7, 6, 5]

# goal2 = [1, 3, 4,
#          8, 0, 6,
#          7, 5, 2]

print(f"test 1: {Dijkstra_Search(initial, goal1)}\nShould be 11\n")
#print(f"test 2: {Dijkstra_Search(initial, goal2)}\nShould be 30")


