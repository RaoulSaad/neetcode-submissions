class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_map ={}
        for i in range(len(board[0])):
            for j in range(len(board[0])):
                square = (i//3)*3 + (j//3)
                row_key = "row" + str(i)
                col_key = "col" + str(j)
                square_key = "square" + str(square)
                if board[i][j] == ".":
                    continue

                if row_key not in hash_map:
                    hash_map[row_key] = [board[i][j]]
                elif board[i][j] in hash_map[row_key]:
                    return False
                else:
                    hash_map[row_key].append(board[i][j])
                
                if col_key not in hash_map:
                    hash_map[col_key] = [board[i][j]]
                elif board[i][j] in hash_map[col_key]:
                    return False
                else:
                    hash_map[col_key].append(board[i][j])
                
                if square_key not in hash_map:
                    hash_map[square_key] = [board[i][j]]
                elif board[i][j] in hash_map[square_key]:
                    return False
                else:
                    hash_map[square_key].append(board[i][j])
        return True

            
