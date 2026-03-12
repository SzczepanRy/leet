class Solution(object):


    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre =list(strs[0])
       # print(pre)
        for i in range(1, len(strs)):
            arr = list(strs[i])
            if(len(arr) < len(pre) ):
                num = len(pre)
            else:
                num = len(arr)
            #print(arr)

            for i in range(1,num+1):

               # print(pre[0:i] , arr[0:i], len(pre[0:i]) ,len(arr) )
                if(pre[0:i] != arr[0:i] or len(pre[0:i])>len(arr) ):
               #     print( "fuck ")
                    pre=arr[0:(i-1)]
              #      print( "fuck " ,pre)
                    break

        print(pre)

        return "".join(pre)

s = Solution()
s.longestCommonPrefix(["ab","a"])

