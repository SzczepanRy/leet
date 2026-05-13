class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp =[0]*n
        dp[0]=1

        i2= 0
        i3= 0
        i5= 0

        for i in range(1,n):
            nt = dp[i2] *2
            nth =dp[i3] *3
            nf = dp[i5] *5

            ug = min(nt , nth , nf)

            dp[i]= ug

            if ug == nt:
                i2+=1
            if ug == nth:
                i3+=1
            if ug == nf:
                i5+=1


        return dp[-1]




s= Solution()
s.nthUglyNumber(10)
