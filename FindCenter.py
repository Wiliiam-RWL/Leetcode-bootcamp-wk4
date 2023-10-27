from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = [0] * (len(edges) + 1)
        for e in edges:
            degree[e[0] - 1] += 1
            degree[e[1] - 1] += 1
            if degree[e[0] - 1] == len(edges):
                return e[0]
            if degree[e[1] - 1] == len(edges):
                return e[1]
        return -1
