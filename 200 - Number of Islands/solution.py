class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows , cols = len(grid) , len(grid[0])
        visited = set()
        islands = 0

        #BFS Function
        def bfs(r, c):
            queue = deque([(r, c)])
            # Mark the starting cell as visited
            grid[r][c] = "0"

            while queue:
                row, col = queue.popleft()

                # Check all 4 possible directions (up, down, left, right)
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    # If the neighbor is within bounds and is land, add to the queue
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1":
                        queue.append((new_row, new_col))
                    # Mark as visited
                        grid[new_row][new_col] = "0"

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    #dfs(r, c)
                    bfs(r, c)
                    islands += 1
        return islands                 
# Below is DFS function 
'''
        def dfs(r, c):
        # If the current cell is out of bounds or water, stop the recursion
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

        # Mark the cell as visited by setting it to "0"
            grid[r][c] = "0"

        # Visit all adjacent cells (up, down, left, right)
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
'''