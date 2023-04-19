import BFS 
import DFS
import DIJKSTRA
import sys

def readFile(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Parse the lines of the file and extract the matrix
    matrix = []
    for line in lines:
        row = line.strip().split()
        for cell in row:
            matrix.append(int(cell))

    # Convert the matrix to a NumPy array
    import numpy as np
    array = np.array(matrix)

    return array

def main():
    # Check if the correct number of arguments were passed
    if len(sys.argv) != 4:
        print("Usage: python script.py <algorithm> <intial_state_file> <goal_state_file>")
        sys.exit(1)

    # Extract the arguments
    algorithm = sys.argv[1]
    initial_state_file = sys.argv[2]
    goal_state_file = sys.argv[3]
    
    initial = readFile(initial_state_file)
    goal = readFile(goal_state_file)

    print(f"this is the intitial state:")
    print(initial)
    DIJKSTRA.print_state(initial)
    print("this is the goal state:")
    print(goal)
    DIJKSTRA.print_state(goal)

    bfs_cost = BFS.Breadth_First_Search(initial, goal)
    dijkstra_cost = DIJKSTRA.Dijkstra_Search(initial, goal)
    dfs_cost = DFS.Depth_First_Search(initial, goal)

    if algorithm == "bfs":
        if bfs_cost == "Unsolvable":
            print("Goal state not found")
        else:
            print("Final cost to reach goal state:", bfs_cost)

    if algorithm == "dfs":
        if dfs_cost == "Unsolvable":
            print("Goal state not found")
        else:
            print("Final cost to reach goal state:", dfs_cost)

    if algorithm == "dijkstra":
        if dijkstra_cost == "Unsolvable":
            print("Goal state not found")
        else:
            print("Final cost to reach goal state:", dijkstra_cost)

main()
