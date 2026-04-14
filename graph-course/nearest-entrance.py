from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """

        visited= [[False ] * len(maze[0]) for _ in range(len(maze))]

        queue = deque([(entrance[0] ,entrance[1], 0)])

        visited[entrance[0]][entrance[1]]=True

        results = []

        while queue:
            r , c , d = queue.popleft()
            for dr , dc in [[0,1] , [1 ,0] , [0,-1] , [-1,0]]:
                nr = r + dr
                nc = c + dc


                if (0 <=nr< len(maze) ) and  (0 <=nc < len(maze[0]) ):

                    if maze[nr ][nc] == "." and not visited[nr][nc] :
                        if nc == 0 or nr == 0 or nc == len(maze[0])-1 or nr == len(maze) -1:
                            # ezit znaleziony
                            results.append(d+1)

                        visited[nr][nc]=True
                        queue.append((nr, nc , d +1))
                        #lecimy dalej

        print(results)

        if len(results) == 0 :
            return -1
        else:
            return min(results)



maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]

maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]

maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
entrance = [0,1 ]

s = Solution()
s.nearestExit(maze , entrance)
