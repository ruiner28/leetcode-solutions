from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def count_live_neighbors(i, j):
            directions = [(-1, -1), (-1, 0), (-1, 1), 
                          (0, -1),        (0, 1), 
                          (1, -1), (1, 0), (1, 1)]
            count = 0
            for x, y in directions:
                ni, nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                    count += 1
            return count

        # Step 1: Modify board using temporary states
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)

                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1  # Mark cell as "was live, now dead"
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2  # Mark cell as "was dead, now live"

        # Step 2: Update the board to final state
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0  # Convert to dead
                elif board[i][j] == 2:
                    board[i][j] = 1  # Convert to live