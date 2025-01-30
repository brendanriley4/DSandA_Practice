import heapq
import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ret = [[]]
        min_heap = []
        for point in points:
            dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(min_heap, (dist, point))
        i = k
        while i > 0:
            temp = heapq.heappop(min_heap)
            ret.append(temp[1])
            i -= 1
        return ret
