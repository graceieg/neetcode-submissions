class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for col in range(9):
            for row in range(9):
                cell = board[row][col]
                box = (row // 3) * 3 + (col // 3)
                if cell == '.': 
                    continue
                else: 
                    #Check row,col,boc
                    if cell in rows[row]:
                        return False
                    if cell in cols[col]: 
                        return False
                    if cell in boxes[box]:
                        return False
                    
                    rows[row].add(cell)
                    cols[col].add(cell)
                    boxes[box].add(cell)
        
        return True


        
                    
