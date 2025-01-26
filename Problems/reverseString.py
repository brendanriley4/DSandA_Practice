from tempfile import tempdir


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        ptr1 = 0
        ptr2 = len(s) - 1
        
        while ptr1 <= ptr2:
            temp = s[ptr1]
            s[ptr1] = s[ptr2]
            s[ptr2] = temp
            ptr1 += 1
            ptr2 -= 1