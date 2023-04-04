
from queue import PriorityQueue

def Dijkstra_Search(initial, goal):
    moves = ['up', 'down', 'left', 'right']

    # Set to keep track of visited states
    visited = set()

    # Priority queue to store states to be visited, with the cost as the priority
    pq = PriorityQueue()
    pq.put((0, initial)) # Add the initial state with a cost of 0

    while not pq.empty():
        cost, curr_state = pq.get() # Get the state with the lowest cost from the priority queue
        
        if curr_state == goal: # If the current state is the goal state, return the cost
            return cost
        
        visited.add(curr_state) # Add the current state to the visited set
        
        zero_index = curr_state.index(0) # Find the index of the empty tile
        
        zero_row, zero_col = divmod(zero_index, 3) # Calculate the row and column of the empty tile

        # Loop through all possible moves
        for move in moves:
            if move == 'up': # If moving the empty tile up
                new_row = zero_row - 1
                new_col = zero_col
            elif move == 'down': # If moving the empty tile down
                new_row = zero_row + 1
                new_col = zero_col
            elif move == 'left': # If moving the empty tile left
                new_row = zero_row
                new_col = zero_col - 1
            elif move == 'right': # If moving the empty tile right
                new_row = zero_row
                new_col = zero_col + 1
            
            # Check if the new row and column are within bounds of the puzzle
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col # Calculate the index of the tile to be swapped with the empty tile
                
                new_state = list(curr_state) # Create a new list to store the new state
                value = new_state[new_index] # Get the value of the tile being swapped
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index] # Swap the tiles
                new_state = tuple(new_state) # Convert the new state back to a tuple
                
                if new_state not in visited: # If the new state has not been visited before
                    pq.put((cost + value, new_state)) # Add the new state with the updated cost to the priority queue 
            else:
                continue # If the new row or column is out of bounds, skip this move
    return "Unsolvable" # If the goal state is not reached, return "Unsolvable"
