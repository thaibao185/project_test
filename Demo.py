# import qrcode

# image = qrcode.make("https://www.facebook.com/bao.thai.73307")
# image.save("qrcode.png", "PNG")

# class Quiz:
#     def __init__(self, question, answer):
#         self.question = question
#         self.answer = answer

# from collections import deque

# def bfs(adj, s, visited):

#     q = deque()
#     visited[s] = True
#     q.append(s)

#     while(q):
#         curr = q.popleft()
#         print(curr, end = " ")
#         for x in adj[curr]:
#             if not visited[x]:
#                 visited[x] = True
#                 q.append(x)

# def add_edge(adj, u, v):
#     adj[u].append(v)
#     adj[v].append(u)

# if __name__ == "__main__":

#     v = 5

#     adj = [[] for _ in range(v)]

#     add_edge(adj, 0, 1)
#     add_edge(adj, 0, 2)
#     add_edge(adj, 1, 3)
#     add_edge(adj, 1, 4)
#     add_edge(adj, 2, 4)

#     visited = [False] * v

#     bfs(adj, 0, visited)

# from sys import*

# class Graph():
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for colum in range(vertices)]
#                       for row in range(vertices)]
    
#     def printSolution(self, dist):
#         print("Vertex\tDistance from Source")
#         for node in range(self.V):
#             print(node, "\t", dist[node])

#     def minDistance(self, dist, sptSet):
#         min = maxsize

#         for u in range(self.V):
#             if dist[u] < min and sptSet[u] == False:
#                 min = dist[u]
#                 min_index = u
#         return min_index
    
#     def dijkstra(self, src):
#         dist = [maxsize] * self.V
#         dist[src] = 0
#         sptSet = [False] * self.V

#         for cout in range(self.V):
#             x = self.minDistance(dist, sptSet)

#             sptSet[x] = True

#             for y in range(self.V):
#                 if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:    
#                     dist[y] = dist[x] + self.graph[x][y]
#         self.printSolution(dist)

# # Driver's code
# if __name__ == "__main__":
#     g = Graph(9)
#     g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#                [4, 0, 8, 0, 0, 0, 0, 11, 0],
#                [0, 8, 0, 7, 0, 4, 0, 0, 2],
#                [0, 0, 7, 0, 9, 14, 0, 0, 0],
#                [0, 0, 0, 9, 0, 10, 0, 0, 0],
#                [0, 0, 4, 14, 10, 0, 2, 0, 0],
#                [0, 0, 0, 0, 0, 2, 0, 1, 6],
#                [8, 11, 0, 0, 0, 0, 1, 0, 7],
#                [0, 0, 2, 0, 0, 0, 6, 7, 0]
#                ]

#     g.dijkstra(0)

from queue import*
from logic import* 

v = 14
graph = [[] for i in range(v)]

def best_first_search(actual_src,  target, n):
    visited = [False]*n
    pq = PriorityQueue()
    pq.put((0, actual_src))

    visited[actual_src] = True

    while pq.empty() == False:
        u = pq.get()[1]
        print(u, end=" ")
        if u == target:
            break
        for v, c in graph[u]:
            # c ở đây là chi phí
            if visited[v] == False:
                visited[v] = True
                pq.put((c,v))

    print()

def addedge(x,y,cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)
 
source = 0
target = 9
best_first_search(source, target, v)