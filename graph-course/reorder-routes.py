class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        adj = [[] for _ in range(n)]

        for curr , to in connections:
            adj[curr].append((to , True)) # [1] czy idzie od zera ( w złym kieruku)
            adj[to].append((curr, False))


        # okreslam w którym grafi do zera odchodzic najwięcej strzałek  (to jest to mniej potymalne )
        visited = [False]*n
        changes = 0

        stack=[0]

        visited[0] = True

        while stack:
            curr = stack.pop()
            for next , isog in adj[curr]:
                if not visited[next]:

                    if isog:
                        changes +=1

                    visited[next]= True
                    stack.append(next)

        return changes










n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
s = Solution()
s.minReorder(n , connections)
