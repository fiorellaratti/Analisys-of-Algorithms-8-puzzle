# 8-Puzzle Solver
link to repo: https://github.com/fiorellaratti/Analisys-of-Algorithms-8-puzzle

This program is a Python implementation of three different algorithms to solve the 8-puzzle problem: Breadth First Search (BFS), Depth First Search (DFS), and Dijkstra's Algorithm. The 8-puzzle is a classic sliding puzzle game consisting of a 3x3 grid of numbered tiles, with one empty space that allows tiles to be moved.

## Getting Started

To run the program, clone the repository and navigate to the project directory in your terminal. Then run the command:

python main.py <algorithm> <start_state_file> <goal_state_file>
Where <algorithm> is one of bfs, dfs, or dijkstra, <start_state_file> is a file containing the initial state of the puzzle, and <goal_state_file> is a file containing the goal state of the puzzle. See the Input Format section for details on how to format these files.

## Algorithms

### Breadth First Search (BFS)
BFS is an uninformed search algorithm that explores all vertices at the current depth level before moving on to vertices at the next depth level. In the context of the 8-puzzle problem, BFS will explore all possible moves from the initial state before exploring moves that are two moves away, three moves away, and so on. This guarantees that the first solution found is the optimal solution.

### Depth First Search (DFS)
DFS is another uninformed search algorithm that explores as far as possible along each branch before backtracking. In the context of the 8-puzzle problem, DFS will explore all possible moves along one branch of the tree before exploring moves along another branch. Unlike BFS, DFS does not guarantee that the first solution found is the optimal solution.

### Dijkstra's Algorithm
Dijkstra's Algorithm is a shortest-path algorithm that finds the shortest path between a source vertex and all other vertices in a weighted graph. In the context of the 8-puzzle problem, Dijkstra's Algorithm assigns a cost to each move based on the number of the moved tile. It then finds the shortest path from the initial state to the goal state based on the sum of the costs of the moves.

## Input Format

The program takes two input files, one containing the initial state of the puzzle and one containing the goal state of the puzzle. The files should be formatted as follows:

<tile> <tile> <tile>
<tile> <tile> <tile>
<tile> <tile> <tile>

Each <tile> is a digit from 0 to 8, where 0 marks the blank space and the other digits are real tiles.

## Output Format

The program outputs the cost of the optimal solution in the terminal/command prompt after running the selected algorithm.

## Example

Suppose we have the following start state:

```
7 2 4
5 0 6
8 3 1
```

And we want to solve the puzzle using BFS and the following goal state:

```
1 3 4
8 0 2
7 6 5
```

We would create two files, start.txt and goal.txt, with the respective states, and then run the command:

```$ python main.py bfs start.txt goal.txt```

The output would be

Shortest path cost: 11

## Contributors

* Kate Anderson
* Fiorella Ratti
* Juan J Gomez