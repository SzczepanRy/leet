

class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """

        outdeg = [0]*n
        is_connected = [[False] *n for _ in range(n)]

        for u,v in roads:
            outdeg[u]+=1
            outdeg[v]+=1
            is_connected[u][v] = True
            is_connected[v][u] = True

        max_rank = 0



        for i in range(n):
            for j in range(i+1,n):
                curr = outdeg[i] + outdeg[j]

                if is_connected[i][j]:
                    curr-=1

                max_rank = max(max_rank, curr)

        return max_rank




n = 5
roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
s=Solution()
s.maximalNetworkRank(n,roads)
