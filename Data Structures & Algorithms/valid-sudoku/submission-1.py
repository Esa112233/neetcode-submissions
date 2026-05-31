class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_dict = {}
        column_dict = {}

        row_len = len(board)
        column_len = len(board[0])

        for i in board:
            dict_in_row = {}
            for num in i:
                if num != ".":
                    if num in dict_in_row:
                        return False
                    else:
                        dict_in_row[num] = 1
        
        for i in range(column_len):
            dict_in_column = {}
            for row in board:
                if row[i] != ".":
                    if row[i] in dict_in_column:
                        return False
                    else:
                        dict_in_column[row[i]] = 1

        
        for c in range(0, 9, 3):
            for r in range(0, 9, 3):
                box_dict = {}
                for j in range(c, c + 3):
                    for i in range(r, r + 3):
                        num = board[i][j]
                        if num != ".":
                            if num in box_dict:
                                return False
                            else:
                                box_dict[num] = 1
                            


        
        return True