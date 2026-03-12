class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        strArr = list(s)
        regArr = list(p)

        conf ={}

        for i in range(len(regArr)):
              if(regArr[i]=="." ):
                conf[i] =[regArr[i-1] , i-1 ]

        for i in range(len(regArr)):
            if( regArr )




s = Solution()
s.isMatch( "aa" , "a*")
