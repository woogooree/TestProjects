from collections import deque

BFS_graph = {'A' : ['B', 'C'],
             'B' : ['D', 'E'],
             'C' : ['F', 'G'],
             'D' : ['B'],
             'E' : ['C'],
             'G' : ['C']}

visited_list = list()

def bfs_func(BFS_graph, start) :
    que = deque([start])

    while que :
        node = que.pop()
        print("node : ", node)

        if node == "E" :
            print("STOP")
            break

        if node not in visited_list :
            visited_list.append(node)
            print(f'방문지점 : {visited_list}')
            que.extendleft(BFS_graph[node])

bfs_func(BFS_graph, 'A')