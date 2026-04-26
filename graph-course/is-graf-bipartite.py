class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        n = len(graph)
        # Tablica kolorów: -1 to brak koloru, 0 i 1 to dwa kolory
        colors = [-1] * n

        def dfs(v, c):
            colors[v] = c
            for neighbor in graph[v]:
                # Jeśli sąsiad ma ten sam kolor co my -> sprzeczność (cykl nieparzysty)
                if colors[neighbor] == c:
                    return False
                # Jeśli sąsiad nie ma koloru -> kolorujemy go kolorem przeciwnym (1-c)
                if colors[neighbor] == -1:
                    if not dfs(neighbor, 1 - c):
                        return False
            return True

        # Dla pewności (nawet jeśli spójny) pętla po wszystkich wierzchołkach
        for i in range(n):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False

        return True




graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph = [[1,3],[0,2],[1,3],[0,2]]
s = Solution()
s.isBipartite(graph)
