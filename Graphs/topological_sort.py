
import heapq as H
from typing import List, Tuple

SEPARATOR: str = "\t"
MAXINT = 10**9
matrix = List[List[int]]


class Graph:
    def __init__(self, n: int, mat: matrix, src: int = 0):
        """
        Create the adjacency list for the given matrix
        :param n: no of nodes
        :param mat: given matrix (m x 3)
        """
        self.adj_list: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        self.adj_list_creator(mat)
        self.visited: List[bool] = [False] * n
        self.q: List[Tuple[int, int]] = []
        self.src: int = src
        self.D: List[int] = [MAXINT] * n

    def adj_list_creator(self, mat: List[List[int]]):
        """
        Creates the adjacency list for given matrix in the format:
        [[vertex1, vertex2, vertex3], [vertex2, vertex3, ...], ...]
        where the index is the vertex and the list at that index has the neighbor vertices.
        :param mat: given matrix (m x 3)
        """
        for i in range(len(mat)):
            v1, v2 = mat[i]
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

    def BFS(self):
        """
        Iterative approach for level order traversal
        """
        level: int = 0
        H.heappush(self.q, (level, self.src))
        self.visited[self.src] = True
        while self.q:
            level, curr_vertex = H.heappop(self.q)
            self.D[curr_vertex] = level
            for nbr in self.adj_list[curr_vertex]:
                if not self.visited[nbr]:
                    H.heappush(self.q, (level + 1, nbr))
                    self.visited[nbr] = True



A = 6
B = [
    [0, 4],
    [3, 4],
    [1, 2],
    [2, 5],
    [2, 4],
    [0, 3],
    [0, 1],
    [4, 5],
    [0, 5]
]
C = 0
G = Graph(A, B, C)
print("Adjacency list: {}".format(G.adj_list))
G.BFS()
print("BFS:")
for vertex, level in enumerate(G.D):
    print("{}NODE-> {} LEVEL-> {}".format(SEPARATOR, vertex, level if level!=MAXINT else "Not Connected"))

