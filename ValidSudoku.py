from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        keys = [str(x) for x in range(1, 10)]
        for x in range(len(board)):
            dict_key_row = {key: 0 for key in keys}
            dict_key_col = {key: 0 for key in keys}
            for y in range(len(board)):
                """
                Each row must contain the digits 1-9 without repetition.
                """
                if board[x][y] != ".":
                    dict_key_row[board[x][y]] += 1
                    if dict_key_row[board[x][y]] > 1:
                        return False
                """
                Each column must contain the digits 1-9 without repetition.
                """
                if board[y][x] != ".":
                    dict_key_col[board[y][x]] += 1
                    if dict_key_col[board[y][x]] > 1:
                        return False
        """
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        """
        keys = [x for x in range(1, 10)]
        count = 0
        for z in range(len(board)):
            if z == 3:
                count += 1
            if z == 6:
                count += 1
            list_value_x = [0, 1, 2, 0, 1, 2, 0, 1, 2]
            list_x = [0, 3, 6, 9]
            dict_key = {str(key): 0 for key in keys}
            for x in range(list_x[list_value_x[z]], list_x[list_value_x[z] + 1]):
                list_value_y = [0, 1, 2]
                list_y = [0, 3, 6, 9]
                for y in range(
                    list_y[list_value_y[count]], list_y[list_value_y[count] + 1]
                ):
                    if board[x][y] != ".":
                        dict_key[board[x][y]] += 1
                        if dict_key[board[x][y]] > 1:
                            return False

        return True


board_ = [
    ["9", ".", ".", "6", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "6", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "1", ".", "3", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "8"],
    [".", ".", ".", ".", ".", "8", ".", ".", "."],
    [".", ".", ".", "4", ".", ".", "2", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "1"],
    ["6", ".", ".", ".", "1", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]
a = Solution()
print(a.isValidSudoku(board=board_))
