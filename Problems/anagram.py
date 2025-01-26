class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        myDict = {}
        i = 0

        if len(s) != len(t):
            return False

        while i < len(s):
            if s[i] in myDict:
                myDict[s[i]] += 1
            else:
                myDict[s[i]] = 1
            i += 1
        j = 0
        while j < len(t):
            if t[j] not in myDict or myDict[t[j]] == 0:
                return False
            myDict[t[j]] -= 1
            j += 1

        return True