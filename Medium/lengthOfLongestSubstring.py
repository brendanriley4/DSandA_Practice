class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        lead, follow = 0, 0
        mySet = {}
        max = 0
        while lead < len(s):
            if s[lead] not in mySet:
                mySet[s[lead]] = lead
                lead += 1
                if lead - follow > max:
                    max = lead - follow
            else:
                if lead - follow > max:
                    max = lead - follow
                follow, lead = mySet[s[lead]], mySet[s[lead]] + 1
                mySet = {}
        return max




if __name__ == '__main__':
    solution = Solution()

    # testCase = "aud"
    # ans = solution.lengthOfLongestSubstring(testCase)
    # print(f"{ans}")

    testCase = "fasdgbttttthjkloiuytredf"
    ans = solution.lengthOfLongestSubstring(testCase)
    print(f"{ans}")