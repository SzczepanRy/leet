class Solution(object):

    def checkArr(self,arr):
        isPallindrome= 1
        for i in range(len(arr)):
#            print(i ,len(arr)-1-i)
            if(arr[i] != arr[len(arr)-1-i]):
                isPallindrome=0
                return []
                #print(i ,len(arr)-1-i)

        if isPallindrome == 1:
#                print (arr )
                return arr
#        print(arr , beginI , endI , isPallindrome)



    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(list(s)) == 1:
            return s

        arr = list(s)
        for i in range(len(arr)):
            for j in range(len(arr)):

                if(len(arr)-i == len(arr[j :(len(arr)-i)+j])):
                  #  print(arr[j :(len(arr)-i)+j])

                    tempArr = self.checkArr(arr[j :(len(arr)-i)+j])
                    if len(tempArr) > 0:
                        return "".join(tempArr)
                else:
                    break




s = Solution()
print(s.longestPalindrome("vmqjjfnxtycii"))


