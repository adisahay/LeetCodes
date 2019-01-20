class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] is not "." and validCell(board, i, j) is False:
                    return False

        return True

def validCell(board, row, col):
    srow = (row // 3) * 3
    scol = (col // 3) * 3

    # Check the block for validity
    for i in range(3):
        for j in range(3):
            if srow + i == row and scol + j == col:
                continue

            if board[srow + i][scol + j] == board[row][col]:
                return False

    # Check the column for validity
    for r in range(9):
        if r is not row and board[r][col] == board[row][col]:
            return False

    # Check the row for validity
    for c in range(9):
        if c is not col and board[row][c] == board[row][col]:
            return False

    return True
