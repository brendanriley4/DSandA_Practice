from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myDict = {}
        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
        ans = len(nums) // 2
        for num in myDict:
            if myDict[num] > ans:
                return num


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([1,1,1,1,1,1,9,9,9,9,9,9,9,9,9,9,9,9]))