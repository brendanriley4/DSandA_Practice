class Solution:
    def hIndex(self, citations):
        if len(citations) == 1:
            if citations[0] == 0: return 0
            else: return 1
        paper_count = [0] * (len(citations) + 1)
        for num in citations:
            if num < len(citations):
                paper_count[num] += 1
            else:
                paper_count[len(citations)] += 1
        h = len(paper_count) - 1
        papers = 0
        while h > 0:
            papers += paper_count[h]
            if papers >= h:
                return h
            h -= 1
        return 0




if __name__ == '__main__':
    solution = Solution()

    testCase = [3,0,6,1,5]
    ans = solution.hIndex(testCase)
    print(f"test case 1: {ans} \n")

    testCase2 = [1,3,9,9,9,9,9,9]
    ans = solution.hIndex(testCase2)
    print(f"test case 2: {ans} \n")

    testCase3 = [1]
    ans = solution.hIndex(testCase3)
    print(f"test case 2: {ans} \n")