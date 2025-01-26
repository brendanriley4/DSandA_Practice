from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Time complexity: O(n^2 log(n))
        # Space complexity: O(n^2)

        n = len(points)

        if n < 2:
            return 0

        min_heap = [(0, 0)] # distance, node connecting to
        cost = 0
        seen_nodes = set()

        while len(seen_nodes) < n:
            dist, i = heapq.heappop(min_heap)

            if i in seen_nodes:
                continue

            seen_nodes.add(i)
            cost += dist
            x_i, y_i = points[i]

            for j in range(n):
                if j not in seen_nodes:
                    x_j, y_j = points[j]
                    nei_dist = abs(x_i - x_j) + abs(y_i - y_j)
                    heapq.heappush(min_heap, (nei_dist, j))

        return cost