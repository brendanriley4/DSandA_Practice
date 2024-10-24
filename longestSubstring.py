import numpy as np

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ""
        minLength = np.inf
        for k in range(len(strs)):
            if len(strs[k]) < minLength:
                minLength = len(strs[k])
        retVal = ""
        i = 0
        j = 0    
        while i < minLength:
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return retVal
                j += 1
            retVal += strs[0][i]
            i += 1
        return retVal

