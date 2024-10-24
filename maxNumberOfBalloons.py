class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        accepted = ['b', 'a', 'l', 'o', 'n']
        myDict = {}
        retVal = 0
        more = True

        for char in text:
            if char in accepted:
                if char in myDict:
                    myDict[char] += 1
                else:
                    myDict[char] = 1

        for char in accepted:
            if char not in myDict:
                return 0

        while more:
            if myDict['b'] > 0 and myDict['a'] > 0 and myDict['l'] > 1 and myDict['o'] > 1 and myDict['n'] > 0:
                retVal += 1
                myDict['b'] -= 1
                myDict['a'] -= 1
                myDict['l'] -= 2
                myDict['o'] -= 2
                myDict['n'] -= 1
            else:
                more = False
        return retVal
