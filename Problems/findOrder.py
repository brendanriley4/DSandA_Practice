from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        order = []
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        print(g)

        states = [UNVISITED] * numCourses

        def dfs(node):
            if states[node] == VISITING:
                return False
            elif states[node] == VISITED:
                return True
            states[node] = VISITING

            for neigh in g[node]:
                if not dfs(neigh):
                    return False

            states[node] = VISITED
            order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order

if __name__ == '__main__':
    solution = Solution()

    tc = [[1,0],[2,0],[3,1],[3,2]]
    print(solution.findOrder(4, tc))