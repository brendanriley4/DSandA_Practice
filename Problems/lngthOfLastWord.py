class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = ""
        length = len(s)
        i = 0
        spaceFound = False
        while i < length:
            if s[i] == " ":
                spaceFound = True
                i += 1
                continue
            elif spaceFound:
                ans = ""
                spaceFound = False
            ans += s[i]
            i += 1
        return len(ans)

if __name__ == '__main__':
    testCase = "hello world penisislong"
    solution = Solution()
    ans = solution.lengthOfLastWord(testCase)
    print(f"{ans}")