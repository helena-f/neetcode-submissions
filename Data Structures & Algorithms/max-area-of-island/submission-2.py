class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        def is_valid_path(row,col):
            if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) 
                    or (row, col) in visited or grid[row][col] != 1):
                    return False
            else:
                return True

        def get_island_area(row, col):    
            visited.add((row,col))
            # up, down, right, left
            directions = [(1,0), (-1, 0), (0,1), (0,-1)]
            area = 1
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                if is_valid_path(new_row, new_col):
                    area += get_island_area(new_row, new_col)
            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if is_valid_path(row, col):
                    val = get_island_area(row, col)
                    max_area = max(val, max_area)
        return max_area