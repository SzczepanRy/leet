from collections import deque
class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)

        sc =0
        sr = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    sc = j
                    sr = i

        visited1 = [[False] *n for _ in range(n)]
        queue = deque([(sr , sc)])

        visited1[sr][sc] = True

        starts = []

        starts.append([sr, sc , 0])

        while queue:
            r ,c = queue.popleft()


            for dr , dc in [[1,0] , [0,1] , [-1,0] , [0,-1 ]]:
                nr = dr + r
                nc = dc + c

                if (0 <= nr < n) and  (0 <= nc < n) :
                    if not visited1[nr][nc] and  grid[nr][nc] == 1:
                        visited1[nr][nc] = True
                        queue.append([nr, nc])
                        starts.append([nr, nc , 0])



        #results = []


        visitedt = [row [:] for row in visited1]
        queuet = deque(starts)


        while queuet:
            r ,c ,d = queuet.popleft()

            for dr , dc in [[1,0] , [0,1] , [-1,0] , [0,-1 ]]:
                nr = dr + r
                nc = dc + c

                if (0 <= nr < n) and  (0 <= nc < n) :
                    if not visitedt[nr][nc] and grid[nr][nc] == 0:
                        visitedt[nr][nc] = True
                        queuet.append([nr, nc , d+1])
                    elif not visitedt[nr][nc] and grid[nr][nc] == 1:
                        #results.append(d)
                        return d



        """
        print(results)
        return min(results)
        """

        return -1








grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
s = Solution()
s.shortestBridge(grid)
