from collections import deque

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        n = len(graph)

        rev= [[] for _ in range(n)]
        out=[0]*n

        for i in range(len(graph)):
            out[i] = len(graph[i])
            for to in graph[i]:
                rev[to].append(i)


        queue = deque([ i for i in range(n) if out[i] == 0 ])

        res = []

        while queue:
            u = queue.popleft()
            res.append(u)
            for v in rev[u]:
                out[v]-=1
                if out[v] == 0 :
                    queue.append(v)

        return sorted(res)






graph = [[1,2],[2,3],[5],[0],[5],[],[]]
s=Solution()
s.eventualSafeNodes(graph)
