class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """

        adj=[[] for _ in range(n)]

        #w zadaniu graf  jest obustronny
        for u , v in connections:
            adj[u].append(v)
            adj[v].append(u)


        d = [-1]* n # czas odwiedzenia
        low = [-1]*n# najniższy czas dotarcia
        parent = [-1 ]* n # rodzice
        time = 0
        res = []

        def dfs(u):
            nonlocal time
            d[u] =low[u]=time
            time+=1

            for v in adj[u]:
                if d[v] == -1:
                    parent[v]= u
                    dfs(v)

                    low[u] =min(low[v],low[u])

                    if d[v] == low[v]:
                        res.append([u,v])
                elif v != parent[u]:
                    #krawędź wsteczna do wierzchołka która nie jest rodzicem
                    low[u] = min(low[u] , d[v])


        for i in range(n):
            if d[i] == -1 :
                dfs(i)

        print(res)
        return res

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

s = Solution()
s.criticalConnections(n , connections)
