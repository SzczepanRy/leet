class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        memo={}

        def rekur(a ,b ):
            if (a,b) in memo:
                return memo[(a,b)]

            if a==b:
                return True

            if sorted(a) != sorted(b):
                return False

            n = len(a)

            res = False

            for  i in range(1,n):

                if rekur(a[:i] ,b[:i]) and rekur(a[i:] ,b[i:]):
                    res = True
                    break

                if rekur(a[:i] ,b[n-i:]) and rekur(a[i:] ,b[:n-i]):
                    res = True
                    break


            memo[(a,b)] = res
            print(memo)

            return res



        return rekur(s1,s2)


s= Solution()
s1 = "greta"
s2 = "rgeat"
print(s.isScramble(s1,s2))

