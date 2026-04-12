from collenction import deque
class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """

        # red 0 blue 1
        out = [[[],[]] for _ in range(n)]

        for i , j in redEdges:
            out[i][0].append(j)
        for i , j in bludeEdges:
            out[i][1].append(j)

        dist = [[float('inf'), float('inf')] for _ in range(n)]

        ## węceł kolor odl
        queue = deque([(0,0,0) , (0,1,0)])

        dist[0][0]=0
        dist[0][1]=0

        while queue:
            curr , lcolor , dis = queue.popleft()

            ncolor  =1 -lcolor

            for next in out[curr][ncolor]:
                if dist[next][ncolor] == float("inf"):
                    dist[next][ncolor] = dis+1
                    queue.append((next, ncolor , dis+1))

        res = []
        for d_red , d_blue in dist:
            m = min(d_red,d_blue)
            res.append(m if m != float("inf") else -1)

        return res
