class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        dp = [0]*n
        dp[0]=1

        inds = [0]*len(primes)

        for i in range(1, n):
            vals = [ dp[inds[j]] * primes[j] for j in range(len(primes)) ]

            mv = min(vals)

            dp[i] = mv

            for k in range(len(vals)):
                if vals[k] == dp[i]:
                    inds[k]+=1

        return dp[-1]




n = 12
primes = [2,7,13,19]
s=Solution()
s.nthSuperUglyNumber(n , primes)
