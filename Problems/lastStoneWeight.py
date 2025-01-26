import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        while len(max_heap) > 1:
            largest = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            if largest == second: continue
            heapq.heappush(max_heap, largest - second)
        if len(max_heap) == 0: return 0
        return -max_heap[0]


if __name__ == '__main__':
    solution = Solution()

    testCase = [2,7,4,1,8,1]
    ans = solution.lastStoneWeight(testCase)
    print(f"test case 1: {ans} \n")

    testCase2 = [1]
    ans = solution.lastStoneWeight(testCase2)
    print(f"test case 2: {ans} \n")

    testCase3 = [1, 1, 1, 8, 9, 27]
    ans = solution.lastStoneWeight(testCase3)
    print(f"test case 2: {ans} \n")
