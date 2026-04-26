from collections import deque
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        visited = [[False]* m for _ in range(n)]


        def count(x,y):

            curr = 1
            queue = deque([(x,y)])
            visited[y][x] = True
            while queue:

                cx ,cy = queue.popleft()
                for dx ,dy in [(1,0),(0,1) , (-1,0)  , (0,-1)]:
                    nx = cx +dx
                    ny = cy +dy
                    if 0<= nx < m and 0<=ny<n:
                        if not visited[ny][nx] and grid[ny][nx]== 1  :
                            visited[ny][nx] = True
                            curr +=1
                            queue.append((nx,ny))

            return curr



        res = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]== 1 and  not visited[y][x]:
                    res = max(res, count(x,y))

        print(res)

        return res

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
s = Solution()
s.maxAreaOfIsland(grid)
