class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #graph problem in which we decide dfs or bfs
        #directions array nsew

        #initialize row/col lengths
        #run bfs on coordinates
        #visit set - if we visit once we wont again

        # initialize a q
        # add the coordinates if they are not in the visit set
        # if value at the coordinates is in the word and the word is non null
        # we'll use a hash set to determine if node val in word
        # find the neighbors and append to the set 

        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r<0 or c<0 or r>=ROWS or c>= COLS or word[i]!=board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'

            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

