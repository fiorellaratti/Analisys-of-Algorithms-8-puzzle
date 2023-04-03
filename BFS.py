import queue

def Breadth_First_Search(initial, goal):
    q = queue.Queue()
    visited = []
    cost = 0

    if initial == goal:
        return 0
    else: 
        while (q.length):
            q.get()
            

def main():
    initial = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]


    print(Breadth_First_Search(initial, goal))

main()