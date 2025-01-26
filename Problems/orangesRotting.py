from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        m, n = len(grid), len(grid[0])
        num_fresh = 0
        que = deque()

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    num_fresh += 1
                elif grid[i][j] == 2:
                    que.append((i, j))

        if num_fresh == 0: return 0
        elif len(que) == 0: return -1

        while que and num_fresh > 0:
            num_rotten = len(que)
            for _ in range(num_rotten):
                i, j = que.popleft()
                for i_off, j_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i+i_off, j+j_off
                    if 0 <= r < m and 0<= c < n and grid[r][c] == 1:
                        que.append((r, c))
                        grid[r][c] = 2
                        num_fresh -= 1
            minutes += 1

        return minutes if num_fresh == 0 else -1

