class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 0 :
            return 0

        res = 0
        i = 1

        while i <= n:
            divider = i* 10
            prefix = n // divider
            digit = (n // i) % 10
            sufix = n % i

            if digit == 0 :
                # tyle cylki ile w prefixie
                res += prefix *i

            elif digit == 1 :
                # pełne z prefix i to co w sufix
                res += prefix * i + (sufix +1 )
            else:
                res += (prefix +1) * i

            i*=10

        return res














n = 13
s=Solution()
print(s.countDigitOne(n))
