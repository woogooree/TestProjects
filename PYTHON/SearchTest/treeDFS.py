DFS_graph = {'A' : ['B', 'C'],
             'B' : ['D', 'E'],
             'C' : ['F', 'G'],
             'D' : ['B'],
             'E' : ['B'],
             'F' : ['C'],
             'G' : ['C']}

visited_list = list()

def dfs_func(DFS_graph, start) :
    visited_list.append(start)
    print(f'방문지점 : {visited_list}')

    for node in DFS_graph[start] :
        print("node : ", node)

        if node == "C" :
            print("STOP")
            break

        # 현재 지점에 방문한 적이 없다면 visited에 추가
        if node not in visited_list :
            dfs_func(DFS_graph, node) #재귀함수

dfs_func(DFS_graph, 'A')