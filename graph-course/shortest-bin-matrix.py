from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if grid[0][0] == 1:
            return -1

        # bsf , po stronach
        n = len(grid)

        dist = [[float("inf")] * n for _ in range(n)]

        # x y d
        queue = deque([(0, 0, 0)])

        while queue:
            cx, cy, cd = queue.popleft()

            if cx == n - 1 and cy == n - 1:
                if dist[cy][cx] == float("inf"):
                    return 1
                print(dist[cy][cx] + 1)
                return dist[cy][cx] + 1

            for rx, ry in [
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 0),
                (-1, -1),
                (0, -1),
                (1, -1),
                (-1, 1),
            ]:
                nx = cx + rx
                ny = cy + ry
                nd = cd + 1

                if 0 <= nx < n and 0 <= ny < n:
                    if grid[ny][nx] == 0 and nd < dist[ny][nx]:
                        dist[ny][nx] = nd
                        queue.append((nx, ny, nd))

        return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
s = Solution()
s.shortestPathBinaryMatrix(grid)
