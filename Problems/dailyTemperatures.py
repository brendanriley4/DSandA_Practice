from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        i = 1
        stack = [(temperatures[0], 0)]
        while i < len(temperatures):
            curr = (temperatures[i], i)
            while stack and curr[0] > stack[-1][0]:
                pop = stack.pop()
                answer[pop[1]] = curr[1] - pop[1]
            stack.append(curr)
            i += 1
        return answer


if __name__ == '__main__':
    solution = Solution()

    testCase = [73,74,75,71,69,72,76,73]
    ans = solution.dailyTemperatures(testCase)
    print(f"test case 1: {ans} \n")

    testCase2 = [30,40,50,60]
    ans = solution.dailyTemperatures(testCase2)
    print(f"test case 2: {ans} \n")

    testCase3 = [30,60,90]
    ans = solution.dailyTemperatures(testCase3)
    print(f"test case 2: {ans} \n")