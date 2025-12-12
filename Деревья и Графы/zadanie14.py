from dataclasses import dataclass
from typing import Optional, List, Dict, Set, Tuple
from collections import deque

from zadanie11 import BST
from zadanie12 import Trie2
from zadanie13 import GraphAdjList, GraphAdjMatrix, bfs, dfs, shortest_path_unweighted
def count_islands(grid):
    if not grid: return 0
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def dfs(i,j):
        stack = [(i,j)]
        visited[i][j] = True
        while stack:
            x,y = stack.pop()
            for dx,dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny]==1:
                    visited[nx][ny] = True
                    stack.append((nx,ny))
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and not visited[i][j]:
                count += 1
                dfs(i,j)
    return count
if __name__ == "__main__":
    print("=== BST demo ===")
    bst = BST()
    for v in [50,30,70,20,40,60,80]:
        bst.insert(v)
    print("inorder:", bst.inorder())
    print("preorder:", bst.preorder())
    print("postorder:", bst.postorder())
    print("search 60:", bool(bst.search(60)))
    print("is balanced:", bst.is_balanced())
    bst.insert(10); bst.insert(5); bst.insert(2)
    print("is balanced after extra inserts:", bst.is_balanced())
    bst.delete(30)
    print("inorder after delete 30:", bst.inorder())

    print("\n=== Trie2 demo ===")
    tr = Trie2()
    words = ["apple","app","application","apt","bat","batch","baton"]
    for w in words:
        tr.insert(w)
    print("count_prefix 'ap':", tr.count_prefix("ap"))
    print("search 'app':", tr.search("app"))
    print("delete 'app':", tr.delete("app"))
    print("search 'app' after delete:", tr.search("app"))
    print("count_prefix 'ap' after delete:", tr.count_prefix("ap"))

    print("\n=== Graph demo ===")
    edges = [(0,1),(0,2),(1,3),(2,4),(3,5)]
    gmat = GraphAdjMatrix(6)
    for u,v in edges: gmat.add_edge(u,v)
    print("BFS mat from 0:", bfs(gmat,0))
    print("DFS mat from 0:", dfs(gmat,0))
    print("shortest path 0->5 (mat):", shortest_path_unweighted(gmat,0,5))

    gal = GraphAdjList(6)
    for u,v in edges: gal.add_edge(u,v)
    print("BFS list from 0:", bfs(gal,0))
    print("DFS list from 0:", dfs(gal,0))
    print("shortest path 0->5 (list):", shortest_path_unweighted(gal,0,5))

    print("\n=== Islands demo ===")
    grid1 = [
        [1,1,0,0,0],
        [1,1,0,1,1],
        [0,0,0,1,1],
        [0,1,0,0,0]
    ]
    print("grid1 islands (expect 2):", count_islands(grid1))
    grid2 = [
        [1,0,1],
        [0,1,0],
        [1,0,1]
    ]
    print("grid2 islands (diagonals not connected, expect 5):", count_islands(grid2))