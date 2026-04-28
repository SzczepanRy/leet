class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        n= len(graph)
        colors = [-1]*n
        colors[0] = 0

        def dfs(v,c):
            for u in graph[v]:
                if colors[u] == -1:
                    colors[u] = c
                    val =dfs(u , 1-c)
                    if not val :
                        return val
                else:
                    if colors[u] != c:
                        return False

            return True




        print(dfs(0,1))










graph = [[1,3],[0,2],[1,3],[0,2]]

graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
s = Solution()
s.isBipartite(graph)
