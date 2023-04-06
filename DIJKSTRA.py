import heapq  # Importing the heapq module for implementing priority queue.

def Dijkstra_Search(initial, goal):
    moves = ['up', 'down', 'left', 'right']  # List of all possible moves.

    # Converting the given initial and goal state lists to tuples for hashing.
    initial = tuple(initial)
    goal = tuple(goal)

    heap = [(0, initial)]  # Initializing a priority queue with initial state and priority 0.
    cost_so_far = {initial: 0}  # Initializing a dictionary to store the cost of each state.

    while heap:
        _, curr_state = heapq.heappop(heap)  # Getting the state with minimum cost from the priority queue.

        if curr_state == goal:  # If the current state is the goal state, return the cost to reach this state.
            return cost_so_far[curr_state]

        zero_index = curr_state.index(0)  # Finding the index of the empty tile (0).

        zero_row, zero_col = divmod(zero_index, 3)  # Finding the row and column of the empty tile.

        for move in moves:  # Looping through all possible moves.
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

            if 0 <= new_row < 3:  # If the new row is within the bounds of the puzzle.
                if 0 <= new_col < 3:  # If the new column is within the bounds of the puzzle.
                    new_index = new_row * 3 + new_col  # Finding the index of the tile to be swapped with the empty tile.

                    new_state = list(curr_state)  # Creating a new state by swapping the empty tile with the tile to be moved.
                    new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                    new_state = tuple(new_state)  # Converting the new state to a tuple.

                    new_cost = cost_so_far[curr_state] + new_state[new_index]  # Calculating the cost to reach the new state.

                    if new_state not in cost_so_far or new_cost < cost_so_far[new_state]:  # If the new state has not been visited before or the new cost is less than the previous cost of the state.
                        cost_so_far[new_state] = new_cost  # Update the cost of the new state.
                        priority = new_cost  # Set the priority of the new state to be the cost.
                        heapq.heappush(heap, (priority, new_state))  # Add the new state to the priority queue with its priority. 

                else:
                    continue
            else:
                continue

    return "Unsolvable"  # If the goal state is not reached, return "Unsolvable".```

#The code uses a priority queue to explore the state space of the 8-puzzle problem in the order of increasing cost to reach each state. 
#The algorithm maintains a dictionary `cost_so_far` to store the cost of each state. 
#The cost of each state is the sum of the costs of the tiles in the state. 
#The algorithm terminates when it reaches the goal state or when it has explored



initial = [7, 2, 4, 
           5, 0, 6, 
           8, 3, 1]

goal1 = [1, 3, 4, 
         8, 0 ,2, 
         7, 6, 5]

goal2 = [1, 3, 4, 
         8, 0, 6, 
         7, 5, 2]

print(f"test 1: {Dijkstra_Search(initial, goal1)}\nShould be 11\n")
print(f"test 2: {Dijkstra_Search(initial, goal2)}\nShould be 30")