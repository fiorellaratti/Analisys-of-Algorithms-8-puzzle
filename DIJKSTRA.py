from queue import PriorityQueue

#helper function
def printQueue(pq):
    if pq.empty():
        print("Priority queue is empty.")
    else:
        items = []
        while not pq.empty():
            items.append(pq.get())
        for item in items:
            print(item)
            pq.put(item)

#helper function
def print_current_state(state):
    print()
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

    # convert the goal state to tuple and use the tuple as comparison key because tuples are immutable
    goal = tuple(goal)

    # initialize a set to track the visited states and a priority queue to store the unvisited ones
    is_visited = set()
    pq = PriorityQueue()

    # initialize a dictionary to track the cost of each state
    costs = {}
    costs[initial] = 0

    pq.put((costs[initial], initial))

    while not pq.empty():
        print("--------------------------")
        #printQueue(pq)
        current_cost, current_state = pq.get()
        print_current_state(current_state)
        if current_state == goal:
            return costs[current_state]

        is_visited.add(current_state)

        # find the index of the black tile
        blank_index = int()
        for i in range(len(current_state)):
            if current_state[i] == 0:
                blank_index = i

        blank_row, blank_col = divmod(blank_index, 3)  # 3 because it's a 3x3 grid

        # itering through each possible move
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

            if 0 <= new_row < 3:
                if 0 <= new_col < 3:
                    new_index = new_row * 3 + new_col
                    new_state = list(current_state)
                    new_state[blank_index] = current_state[new_index]
                    new_state[new_index] = current_state[blank_index]
                    new_state = tuple(new_state)

                    if new_state not in is_visited:
                        # calculate cost of moving to new state
                        move_cost = new_state[blank_index]
                        new_cost = costs[current_state] + move_cost

                        # update the cost of the new state in the dictionary
                        if new_state not in costs or new_cost < costs[new_state]:
                            costs[new_state] = new_cost

                            # add new state to priority queue with updated cost
                            pq.put((new_cost, new_state))

        # reverse the order of moves so that it tries to go in a different direction in the next iteration
        moves.reverse()
    return "Unsolvable"


initial = [7, 2, 4,
           5, 0, 6,
           8, 3, 1]

goal1 = [1, 3, 4,
         8, 0, 2,
         7, 6, 5]

goal2 = [1, 3, 4,
         8, 0, 6,
         7, 5, 2]

#print(f"test 1: {Dijkstra_Search(initial, goal1)}\nShould be 11\n")
print(f"test 2: {Dijkstra_Search(initial, [1, 3, 4, 8, 0, 2, 7, 6, 5])}\nShould be 30")

