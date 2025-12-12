from dataclasses import dataclass
from typing import Optional, List, Dict, Set, Tuple
from collections import deque
class GraphAdjMatrix:
    def __init__(self, n):
        self.n = n
        self.mat = [[0]*n for _ in range(n)]

    def add_edge(self, u, v):
        self.mat[u][v] = 1
        self.mat[v][u] = 1  

    def neighbors(self, u):
        for v in range(self.n):
            if self.mat[u][v]:
                yield v

class GraphAdjList:
    def __init__(self, n):
        self.n = n
        self.adj: Dict[int, List[int]] = {i: [] for i in range(n)}

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  

    def neighbors(self, u):
        return iter(self.adj[u])

def bfs(graph, start) -> List[int]:
    visited = [False]*graph.n
    order = []
    q = deque([start])
    visited[start] = True
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.neighbors(u):
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return order

def dfs(graph, start) -> List[int]:
    visited = [False]*graph.n
    order = []
    stack = [start]
    while stack:
        u = stack.pop()
        if visited[u]: 
            continue
        visited[u] = True
        order.append(u)
        for v in reversed(list(graph.neighbors(u))):
            if not visited[v]:
                stack.append(v)
    return order

def shortest_path_unweighted(graph, start, target) -> Optional[List[int]]:
    if start == target:
        return [start]
    visited = [False]*graph.n
    parent = [-1]*graph.n
    q = deque([start])
    visited[start] = True
    while q:
        u = q.popleft()
        for v in graph.neighbors(u):
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                if v == target:
                    path = [v]
                    while parent[path[-1]] != -1:
                        path.append(parent[path[-1]])
                    return list(reversed(path))
                q.append(v)
    return None