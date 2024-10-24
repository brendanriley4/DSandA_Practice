class Solution(object):
    def isSubsequence(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        index = 0
        for i in s:
            if i in t[index:]:
                index = t[index:].index(i)
            else:
                return False
        return True
