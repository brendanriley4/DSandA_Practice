class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # rows
        rowDict = {}
        i, j = 0, 0
        while i < len(board):
            while j < len(board):
                if board[i][j] == ".":
                    j += 1
                    continue
                if board[i][j] in rowDict:
                    return False
                rowDict[board[i][j]] = 1
                j += 1
            rowDict = {}
            j = 0
            i += 1

        # columns
        colDict = {}
        i, j = 0, 0
        while i < len(board):
            while j < len(board):
                if board[j][i] == ".":
                    j += 1
                    continue
                if board[j][i] in rowDict:
                    return False
                rowDict[board[j][i]] = 1
                j += 1
            rowDict = {}
            j = 0
            i += 1

        lenSud = len(board) / 3
        i, j, k, l = 0, 0, 0, 0
        sudDict = {}
        while k < lenSud:
            while l < lenSud:
                i, j = l*3, k*3
                while i < l*3+3:
                    while j < k*3+3:
                        # print(f"Seen: {board[i][j]}")
                        # print(f"{sudDict}")
                        print(f"{i, j, k, l}")
                        if board[i][j] == ".":
                            j += 1
                            continue
                        if board[i][j] in sudDict:
                            return False
                        sudDict[board[i][j]] = 1
                        j += 1

                    j = k*3
                    i += 1
                sudDict = {}
                i = l*3
                l += 1
            l = 0
            k += 1

        return True



if __name__ == '__main__':
    solution = Solution()

    testCase = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    ans = solution.isValidSudoku(testCase)
    print(f"test case 1: {ans} \n")

    testCase2 = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["2",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    ans = solution.isValidSudoku(testCase2)
    print(f"test case 2: {ans} \n")

    testCase3 = [[".",".",".",".","5",".",".","1","."],
                 [".","4",".","3",".",".",".",".","."],
                 [".",".",".",".",".","3",".",".","1"],
                 ["8",".",".",".",".",".",".","2","."],
                 [".",".","2",".","7",".",".",".","."],
                 [".","1","5",".",".",".",".",".","."],
                 [".",".",".",".",".","2",".",".","."],
                 [".","2",".","9",".",".",".",".","."],
                 [".",".","4",".",".",".",".",".","."]]
    ans = solution.isValidSudoku(testCase3)
    print(f"test case 3: {ans} \n")