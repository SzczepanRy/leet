from collections import deque
class Solution():
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        adj = [[] for _ in range(n)]

        for u ,v in edges:
            adj[u].append(v)

        indeg = [0]*n

        for arr in adj:
            for v in arr:
                indeg[v]+=1

        queue = deque([i for i in range(n) if indeg[i] == 0])

        toporder = []

        while queue:

            v = queue.popleft()
            toporder.append(v)

            for u in adj[v]:
                indeg[u]-=1

                if indeg[u]==0:
                    queue.append(u)

        # jesli to dag , to długośc topoorder powinno bć równe n
        visited = [False]*n

        res = []

        for i in toporder:
            if not visited[i]:
                res.append(i)
                queue = deque([i])
                visited[i] = True

                while queue:
                    c = queue.popleft()
                    for n in adj[c]:
                        if not visited[n]:
                            visited[n] = True
                            queue.append(n)


        #print(toporder)
        #print(res)

        return res


n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
s= Solution()
s.findSmallestSetOfVertices(n , edges)
