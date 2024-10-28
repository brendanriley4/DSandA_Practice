class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myDict = {}
        length = len(nums)
        for num in nums:
            if num not in myDict:
                myDict[num] = 1
            else:
                myDict[num] += 1
            if myDict[num] > (length / 2):
                return num

if __name__ == '__main__':
    testCase = [2,2,1,1,1,2,2]
    solution = Solution()
    ans = solution.majorityElement(testCase)
    print(f"{ans}")