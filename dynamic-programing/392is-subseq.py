class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == 0:
            return True


        i = 0
        j = 0

        n =len(t)


        while j < n :
            if s[i] == t[j]:
                i+=1
                print(i , j )
                if i == len(s):
                    return True

            j+=1

        return False





s=Solution()
print(s.isSubsequence("abc" , "ahbgdc"))
