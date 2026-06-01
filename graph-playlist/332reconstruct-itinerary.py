class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj = {}

        for u, v in tickets:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)

        for src in adj:
            adj[src].sort(reverse=True)

        result = []

        def dfs(u):
            while adj[u]:
                next_dest = adj[u].pop()
                dfs(next_dest)

            result.append(u)

        dfs("JFK")

        return result[::-1]







tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

s = Solution()
s.findItinerary(tickets)
