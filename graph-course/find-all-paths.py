
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        # zaczynam zawsze od zera
        # dag bez cykli nie trzeba visited

        # DFS z backtrakingiem
        n = len(graph)
        res = []

        def DFS(u , p):
            if u == n-1 :
                res.append(p[:])
                return

            for v in graph[u]:
                p.append(v)
                DFS(v , p)
                p.pop()


        DFS(0 ,[0])

        return res










graph = [[4,3,1],[3,2,4],[3],[4],[]]
s = Solution()
s.allPathsSourceTarget(graph)
