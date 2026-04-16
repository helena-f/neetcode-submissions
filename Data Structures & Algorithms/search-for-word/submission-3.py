class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # edge cases:
        # empty board, size 1 board, invalid board
        # empty word, word of size 1

        # iterate through each letter in the array to find the start of the word
        # for loops until matching first char

        # start a dfs search for the subsequent letters - returning True/False
        # manage visited so no cycles form, unique to the current search of word
        # search up down, left right
        # if found next char, call the dfs on the next coordinate
        # if not, clear visited, and return False
        # return if you've found the word

        # stay within bounds
        rowsnum = len(board)
        colsnum = len(board[0])

        visited = set()
        def dfs(row, col, index):
            if index >= len(word):
                return True

            visited.add((row, col))
            directions = [[0,-1], [-1,0], [1,0], [0,1]]
            # if one of the four directions works, good. if not, false
            for r, c in directions:
                newrow = r + row
                newcol = c + col
                # check if new index is in bounds
                if ((newrow, newcol) not in visited 
                    and 0 <= newrow < rowsnum and 0 <= newcol < colsnum):
                    
                    if word[index] == board[newrow][newcol]:
                        if dfs(newrow, newcol, index + 1):
                            visited.remove((row,col))
                            return True
                        
            visited.remove((row,col))
            return False


        for row in range(rowsnum):
            for col in range(colsnum):
                if board[row][col] == word[0] and dfs(row, col, 1):
                    return True
      
        print("did not find word")
        return False