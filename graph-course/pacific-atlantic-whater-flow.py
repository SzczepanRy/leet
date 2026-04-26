from collections import deque
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(heights)
        m = len(heights[0])

        def whaterflow(x , y ):

            visited = set()
            visited.add((x,y))
            queue= deque([(x,y, heights[y][x])])

            pa = False
            at = False

            while queue:

                cx , cy , h = queue.popleft()


                if cx == 0 or cy == 0:
                    pa = True
                if cx == m - 1 or cy == n - 1:
                    at = True

                for dx ,dy in [(1,0) , (0,1) , (-1,0) , (0,-1)]:
                    nx = cx+ dx
                    ny = cy+ dy
                    if 0<= nx <m  and 0<= ny < n:
                        if (nx,ny) not in visited:
                            nh = heights[ny][nx]
                            if nh <= h:
                                visited.add((nx,ny))
                                queue.append((nx,ny,nh))

            return all([pa , at])


        res = []
        for y in range(n-1,-1,-1):
            for x in range(m-1,-1,-1):
                if y == 0 and x == m-1:
                    res.append([y,x])
                elif y == n-1 and x == 0:
                    res.append([y,x])
                elif whaterflow(x,y):
                    res.append([y,x])


        res.sort()
        print(res)
        return res


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
s = Solution()
s.pacificAtlantic(heights)
