class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = [False]*len(isConnected)
        count = 0

        def DFS(v):

            visited[v] = True
            for u in range(len(isConnected[v])):
                if isConnected[v][u] == 1 and not visited[u]:
                    DFS(u)

        for i in range(len(isConnected)):
            if not visited[i]:
                count +=1
                DFS(i)

        return count

isConnected = [[1,1,0],[1,1,1],[0,1,1]]
s = Solution()
s.findCircleNum(isConnected)





