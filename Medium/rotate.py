class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        i, j = 0, 0
        while i < len(matrix): # transpose the matrix!
            while j < len(matrix):
                if i == j:
                    j += 1
                else:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
                    j += 1
            i += 1
            j = i

        i, j, k = 0, len(matrix) - 1, 0
        while k < len(matrix):
            while j - i > 0 and i < len(matrix):
                temp = matrix[k][i]
                matrix[k][i] = matrix[k][j]
                matrix[k][j] = temp
                i += 1
                j -= 1
            k += 1
            i = 0
            j = len(matrix) - 1

        return matrix




if __name__ == '__main__':
    solution = Solution()

    testCase = [[1,2,3],[4,5,6],[7,8,9]]
    ans = solution.rotate(testCase)
    print(f"test case 1: {ans}, \n")

    testCase2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    ans = solution.rotate(testCase2)
    print(f"test case 1: {ans}, \n")

    # testCase3 = "(("
    # ans = solution.isValid(testCase3)
    # print(f"test case 3: {ans} \n")