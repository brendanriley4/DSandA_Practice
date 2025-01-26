import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        while k > 1:
            heapq.heappop(max_heap)
            k -= 1
        kth = -heapq.heappop(max_heap)
        return kth

if __name__ == '__main__':
    solution = Solution()

    tc1 = [3,2,1,5,6,4]
    k1 = 2
    print(solution.findKthLargest(tc1, k1))

    print("")

    tc2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    print(solution.findKthLargest(tc2, k2))
