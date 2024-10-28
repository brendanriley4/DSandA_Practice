class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        retVal = []
        m, n = len(matrix), len(matrix[0])
        totalLength = m * n
        up, right, left, down = 0, 1, 2, 3
        direction = right
        upWall = 0
        rightWall = n
        leftWall = -1
        downWall = m
        i, j = 0, 0

        # O(m * n)
        while len(retVal) != totalLength:
            if direction == right:
                while i < rightWall:
                    retVal.append(matrix[j][i])
                    i += 1
                direction = down
                i -= 1
                j += 1
                rightWall -= 1
            elif direction == down:
                while j < downWall:
                    retVal.append(matrix[j][i])
                    j += 1
                direction = left
                i = i - 1
                j = j - 1
                downWall -= 1
            elif direction == left:
                while i > leftWall:
                    retVal.append(matrix[j][i])
                    i -= 1
                direction = up
                i += 1
                j -= 1
                leftWall += 1
            elif direction == up:
                while j > upWall:
                    retVal.append(matrix[j][i])
                    j -= 1
                direction = right
                i += 1
                j += 1
                upWall += 1
        return retVal

if __name__ == '__main__':
    testCase = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    solution = Solution()
    ans = solution.spiralOrder(testCase)