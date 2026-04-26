class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        p , j = trust[0]

        s= set()
        if j == p:
            return -1
        s.add(p)

        for i in range(1,len(trust)):
            a, b = trust[i]

            if b !=  j :
                return -1
            if a == j :
                return -1
            s.add(a)

        for i in range(1,n):
            if i not in s and i != j:
                return -1

        print(j)
        return j




n = 3
trust = [[1,3],[2,3],[3,1]]
s = Solution()
s.findJudge(n, trust)
