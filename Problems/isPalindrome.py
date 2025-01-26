import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.replace(" ", "")
        s = s.lower()
        if len(s) == 0:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    solution = Solution()

    testCase = "A man, a plan, a canal: Panama"
    ans = solution.isPalindrome(testCase)
    print(f"test case 1: {ans}, Expected = True\n")

    testCase2 = "race a car"
    ans = solution.isPalindrome(testCase2)
    print(f"test case 2: {ans}, Expected: False\n")

    testCase3 = " "
    ans = solution.isPalindrome(testCase3)
    print(f"test case 3: {ans}, Expected = True\n")