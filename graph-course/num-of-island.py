from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        visited= [[False]*m for _ in range(n)]

        def BFS( sx , sy ):

            visited[sy][sx]= True
            queue = deque([(sx,sy)])


            while queue:
                cx , cy = queue.popleft()

                for xd ,yd  in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nx  = cx + xd
                    ny  = cy + yd

                    if 0<= nx < m and 0<= ny <n:
                        if not visited[ny][nx] and grid[ny][nx] == "1" :
                            visited[ny][nx]= True
                            queue.append((nx,ny))
        count = 0

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j]=="1":
                    BFS( j , i )
                    count +=1

        print(count)
        return count



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

s=Solution()
s.numIslands(grid)
