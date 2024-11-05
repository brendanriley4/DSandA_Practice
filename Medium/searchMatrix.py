class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # my idea: find row and then find column? Might be better idea then jumping both
        # matrices are [Row][Column]

        leftRow, rightRow = 0, len(matrix) - 1
        while leftRow <= rightRow:
            midRow = (leftRow + rightRow) // 2
            if matrix[midRow][0] == target:
                return  True
            if matrix[midRow][0] <= target <= matrix[midRow][-1]:
                break
            elif matrix[midRow][0] < target:
                leftRow = midRow + 1
            else:
                rightRow = midRow - 1

        leftCol, rightCol = 0, len(matrix[0]) - 1
        while leftCol <= rightCol:
            midCol = (leftCol + rightCol) // 2
            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] < target:
                leftCol = midCol + 1
            else:
                rightCol = midCol - 1

        return False

if __name__ == '__main__':
    solution = Solution()

    testCase = [[1]]
    n = 3
    ans = solution.searchMatrix(testCase, n)
    print(f"{ans}")

    testCase = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    n = 3
    ans = solution.searchMatrix(testCase, n)
    print(f"{ans}")