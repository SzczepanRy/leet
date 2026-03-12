class Solution(object):
    def lengthOfLongestSubstring(self, s):

        a = r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """
        print(a)
        arr= list(s)

        if( len(arr) == 1 ):
            return 1
        if( len(arr) == len(set(arr))):
            return len(arr)




        maxlen =0
        for i in range(len(arr)):
            for j in range(len(arr)-i):
                print(arr[i:len(arr)-j])
                if( len(arr[i:len(arr)-j]) < maxlen  ):
                    break
                elif( len(arr[i:len(arr)-j]) == len(set(arr[i:len(arr)-j])) ):
                    maxlen = len(arr[i:len(arr)-j])

        return maxlen

s = Solution()
print(s.lengthOfLongestSubstring(""))
