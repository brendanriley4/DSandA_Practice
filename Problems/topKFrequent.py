import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        myDict = {}
        for num in nums:
            myDict[num] = myDict.get(num, 0) + 1
        max_heap = [(-freq, num) for num, freq in myDict.items()]
        heapq.heapify(max_heap)
        i = 0
        while i < k:
            ret.append(heapq.heappop(max_heap)[1])
            i +=1
        return ret

if __name__ == '__main__':

    solution = Solution()

    tc = [1,1,1,2,2,3]
    k = 2
    ans = solution.topKFrequent(tc, k)
    print(ans)