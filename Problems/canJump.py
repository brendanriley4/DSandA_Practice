from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        num_jumps = 1
        i = len(nums) - 2
        while i > -1:
            if nums[i] >= num_jumps:
                num_jumps = 0
            i -= 1
            num_jumps += 1
        print(num_jumps)
        return num_jumps == 1


        # WE CAN DO BETTER THAN BRUTE FORCE RECURSION!!!
        # is_possible = [False]
        #
        # def recurse(index):
        #     if index >= len(nums) - 1:
        #         is_possible[0] = True
        #         return
        #     if is_possible[0]:
        #         return
        #     for i in range(1, nums[index] + 1):
        #         recurse(index + i)
        #
        # recurse(0)
        # return is_possible[0]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.canJump([3,2,1,0,0,0,0,0,0,0,4])
    print(ans)