class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        myLetters = {}
        i, j = 0, 0

        while j < len(magazine):
            if magazine[j] in myLetters:
                myLetters[magazine[j]] += 1
            else:
                myLetters[magazine[j]] = 1
            j += 1

        while i < len(ransomNote):
            if ransomNote[i] not in myLetters or myLetters[ransomNote[i]] == 0:
                return False
            myLetters[ransomNote[i]] -= 1
            i += 1
        return True