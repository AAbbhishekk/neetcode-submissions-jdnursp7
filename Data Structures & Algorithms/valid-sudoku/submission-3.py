class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_check =defaultdict(set)
        columns_check = defaultdict(set)
        cells_check = defaultdict(set)


   

        rows = len(board)
        columns = len(board[0])

        for r in range(rows):
            for c in range(columns):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows_check[r] or board[r][c] in columns_check[c] or board[r][c] in cells_check[(r//3),c//3]):
                    return False
                
                rows_check[r].add(board[r][c])
                columns_check[c].add(board[r][c])
                cells_check[(r//3,c//3)].add(board[r][c])
        return True
            


                


        