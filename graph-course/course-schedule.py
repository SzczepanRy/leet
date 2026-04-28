from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adj =[[]for _ in range(numCourses)]


        indeg = [0]*numCourses
        for v, u in prerequisites:
            adj[u].append(v)
            indeg[v]+=1

        queue= deque([i for i in range(len(indeg)) if indeg[i] == 0])

        topoord=[]
        while queue:
            c = queue.popleft()
            topoord.append(c)

            for v in adj[c]:
                indeg[v]-=1
                if indeg[v]==0:
                    queue.append(v)

        #print(topoord)
        if len(topoord) == numCourses:
            return True
        return False




numCourses = 3
prerequisites = [[1,0],[0,1] ,[1,2]]
s = Solution()
s.canFinish(numCourses, prerequisites )
