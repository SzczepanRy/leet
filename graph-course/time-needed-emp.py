from collections import deque
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        ## men -> emp
        out= [[] for _ in range(n)]

        for emp , men in  enumerate(manager):
            if men != -1:
                out[men].append(emp)


        queue = deque([(headID,0)])
        maxT= 0

        while queue:
            parent , time = queue.popleft()

            maxT= max(maxT , time)

            for e  in out[parent]:
                queue.append((v, time+ informTime[parent]))

        return maxT

n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]
s = Solution()
s.numOfMinutes(n , headID, manager , informTime)
