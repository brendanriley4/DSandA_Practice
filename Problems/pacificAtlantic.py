from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_que = deque()
        a_que = deque()
        p_seen = set()
        a_seen = set()
        m, n = len(heights), len(heights[0])

        for j in range(n):
            p_que.append((0, j))
            p_seen.add((0, j))
            a_que.append((m-1, j))
            a_seen.add((m-1, j))

        for i in range(m):
            p_que.append((i, 0))
            p_seen.add((i, 0))
            a_que.append((i, n-1))
            a_seen.add((i, n-1))

        def getCoords(que, seen):
            while que:
                i, j = que.popleft()
                for i_off, j_off in [(0,1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i+i_off, j+j_off
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        seen.add((r, c))
                        que.append((r, c))

        getCoords(p_que, p_seen)
        getCoords(a_que, a_seen)

        return list(p_seen & a_seen)
