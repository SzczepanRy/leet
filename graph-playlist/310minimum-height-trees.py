from collections import deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        """
        adj = [[] for _ in range(n)]

        for u ,v in edges:
            adj[u].append(v)
            adj[v].append(u)


        print(adj)

        def height(start):
            ## mst bedzie dobre
            #queue = deque([adj[start]])
            def dfs(u,p):
                m = 0
                for v in adj[u]:
                    if v != p:
                        np = u
                        m = max(m , dfs(v ,np) +1 )

                return m

            return dfs(start,-1)

        res = [0]*n
        for i in range(n):
            res[i]=height(i)

        r = min(res)

        result = []

        for i in range(n):
            if res[i] == r:
                result.append(i)

        return result

        """

        if n <= 2 :
            return [i for i in range(n)]

        adj =[set() for _ in range(n)]

        for u , v in edges:
            adj[u].add(v)
            adj[v].add(u)

        leaves = deque()
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)

        remaining = n
        while remaining >2:
            lcount = len(leaves)
            remaining -=lcount

            for _ in range(lcount):
                leaf = leaves.popleft()

                neighbor = adj[leaf].pop()

                adj[neighbor].remove(leaf)# dla tego set

                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)



n = 4
edges = [[1,0],[1,2],[1,3]]

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

s = Solution()
print(s.findMinHeightTrees(n , edges))
