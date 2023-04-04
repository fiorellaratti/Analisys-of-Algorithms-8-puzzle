import BFS 
import DFS
import DIJKSTRA


def main():
    initial = (7, 2, 4, 5, 0, 6, 8, 3, 1)
    
    goal1 = (1, 3, 4, 8, 0 ,2, 7, 6, 5)
    
    goal2 = (1, 3, 4, 8, 0, 6, 7, 5, 2)

    bfs_cost_1 = BFS.Breadth_First_Search(initial, goal1)
    dfs_cost_1 = DFS.Depth_First_Search(initial, goal1)
    dijkstra_cost_1 = DIJKSTRA.Dijkstra_Search(initial, goal1)

    print("Solution for sample 1: ", goal1)

    if bfs_cost_1 == "Unsolvable":
        print("Goal state not found")
    else:
        print("Final cost to reach goal state using BFS:", bfs_cost_1)

    if dfs_cost_1 == "Unsolvable":
        print("Goal state not found")
    else:
        print("Final cost to reach goal state using DFS:", dfs_cost_1)

    if dijkstra_cost_1 == "Unsolvable":
        print("Goal state not found")
    else:
        print("Final cost to reach goal state using Dijkstra's:", dijkstra_cost_1)

    
    bfs_cost_2 = BFS.Breadth_First_Search(initial, goal2)
    dfs_cost_2 = DFS.Depth_First_Search(initial, goal2)
    dijkstra_cost_2 = DIJKSTRA.Dijkstra_Search(initial, goal2)

    print("\nSolution for sample 2: ", goal2)

    if bfs_cost_2 == "Unsolvable":
        print("Goal state not found")
    else:
        print("Final cost to reach goal state using BFS:", bfs_cost_2)

    if dfs_cost_2 == "Unsolvable":
        print("Goal state not found")
    else:
        print("Final cost to reach goal state using DFS:", dfs_cost_2)

    if dijkstra_cost_2 == "Unsolvable":
        print("Goal state not found")
    else:
        print("Final cost to reach goal state using Dijkstra's:", dijkstra_cost_2)




main()
