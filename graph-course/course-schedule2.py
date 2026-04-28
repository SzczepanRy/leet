from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        n = numCourses
        edges = prerequisites
        indeg = [0] *n

        adj = [[] for _ in range(n)]

        for u , v in edges:
            adj[v].append(u)
            indeg[u]+=1


        q = deque([i for i in range(n) if indeg[i] == 0])

        order=[]
        while q:
            c = q.popleft()
            order.append(c)
            for u in adj[c]:
                indeg[u]-=1

                if indeg[u]==0:
                    q.append(u)

        print(order)
        if len(order) != n:
            return []
        return order


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
numCourses  = 3
prerequisites =[[1,0],[1,2],[0,1]]
s = Solution()
s.findOrder(numCourses ,prerequisites )

