import BFS 
# import DFS
# import DIJKSTRA


def main():
    initial = [1, 3, 4, 8, 0, 2, 7, 6, 5]
    goal = [1, 2, 3, 8, 0 ,4, 7, 6, 5]

    bfs_cost = BFS.Breadth_First_Search(initial, goal)
    #dfs_cost = DFS.Depth_First_Search(initial, goal)
    #dijkstra_cost = DIJKSTRA.Dijkstra_Search(initial, goal)
    


    if bfs_cost == "Unsolvable":
        print("Goal state not found")
    else:
        print("Final cost to reach goal state:", bfs_cost)





main()
