from collections import deque
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]


        def BFS (x, y ):
            visited[y][x] = True

            queue = deque([(x,y )])

            while queue:
                cx,cy = queue.popleft()

                for dx , dy in [(1,0),(0,1) , (-1,0) , (0,-1)]:
                    nx = cx +dx
                    ny = cy +dy

                    if 0<= nx < m and 0<= ny < n:
                        if not visited[ny][nx] and grid[ny][nx] == 0:
                            visited[ny][nx] = True
                            queue.append((nx,ny))
            return

        # usuwam wszystkie lądy u brzegów

        for y in range(n):
            for x in [0, m - 1]:
                if grid[y][x] == 0 and not visited[y][x]:
                    BFS(x, y)

        for x in range(m):
            for y in [0, n - 1]:
                if grid[y][x] == 0 and not visited[y][x]:
                    BFS(x, y)

        res = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == 0 and not visited[y][x]:
                    BFS(x, y)
                    res+=1
        print(res)
        return res



grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
s = Solution()
s.closedIsland(grid)
