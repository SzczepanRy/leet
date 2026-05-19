class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        memo = {1:0}

        def rekur(i):
            if i in memo :
                return memo[i]

            if i % 2 == 0:
                memo[i] = rekur(i//2)+1
            else:
                memo[i]= min(rekur(i+1) , rekur(i-1))+1

            return memo[i]

        return rekur(n)

s = Solution()
print(s.integerReplacement(7))
