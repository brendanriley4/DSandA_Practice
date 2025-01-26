class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        myJewels = {}
        retVal = 0

        for char in jewels:
            myJewels[char] = 0

        for char in stones:
            if char in myJewels:
                myJewels[char] = myJewels.get(char) + 1

        for value in myJewels.values():
            retVal += value

        return retVal