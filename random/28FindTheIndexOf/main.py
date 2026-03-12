class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(len(haystack) < len(needle)):
            return -1
        for i in range(len(haystack)):
            if(haystack[i] == needle[0]):
                isGood= True
                for j in range(len(needle)):
                    try:
                        if(haystack[i+j] != needle[j]):
                            isGood =False
                    except:
                        return -1
                if(isGood):
                    #print(i)
                    return i
        #print(-1)
        return -1

s = Solution()
s.strStr("leetcode", "sad")

