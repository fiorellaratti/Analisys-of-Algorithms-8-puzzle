
from queue import Queue

def Breadth_First_Search(initial, goal):
    # Define the four possible moves (up, down, left, right)
    moves = ['up', 'down', 'left', 'right']

    # Initialize a set to keep track of visited states and a queue to hold the states to explore
    visited = set()
    q = Queue()

    # Convert the initial state and goal state to tuples and add the initial state to the queue with a cost of 0
    q.put((initial, 0))

    # Loop until the queue is empty
    while not q.empty():
        # Get the next state to explore and its cost
        curr_state, cost = q.get()
        
        # If we have reached the goal state, return the cost to reach it
        if curr_state == goal:
            return cost
        
        # Add the current state to the set of visited states
        visited.add(curr_state)
        
        # Find the index of the zero (empty) tile in the current state
        zero_index = curr_state.index(0)
        
        # Convert the zero index to a row and column
        zero_row, zero_col = divmod(zero_index, 3)

        # Loop over the four possible moves
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
            
            # Check if the new row and column are within the bounds of the puzzle
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Convert the new row and column to an index
                new_index = new_row * 3 + new_col
                    
                # Create a new state by swapping the zero tile with the tile in the new position
                new_state = list(curr_state)
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                new_state = tuple(new_state)
                    
                # If the new state has not been visited, add it to the queue with a cost of one more than the current cost
                if new_state not in visited:
                    q.put((new_state, cost + 1)) 
            else:
                continue
    # If we have explored all possible states and not found the goal, return "Unsolvable"
    return "Unsolvable"