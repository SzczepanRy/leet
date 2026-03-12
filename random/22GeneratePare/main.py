class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        obj = {}
        for a in range(n**2):
            obj[a] =[]
            for b in range(n*2):
                obj[a].append("")
            array = obj[a]
        for c in range(n):
            for d in range(1,n):
                obj[c][d-1]="("
            print(c , n)
            obj[c][n+c-1]="("

        for c in range(3,n+3):
            for d in range(1,n-1):
                obj[c][d-1]="("
            print(c , n)
            for f in range(n-1):
                obj[c][f+n+c-1 -3]="("





        print(obj)



s = Solution()
s.generateParenthesis(3)
