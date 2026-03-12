class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = str(x)
        arr = list(s)
        l = len(arr)-1
        tempArr = []
        for i in range(len(arr)):
            tempArr.append(arr[l-i])


        if(x < 0):
            tempArr.pop()
            st = "-"+"".join(tempArr)
            if (int(st) < pow(-2, 31)):
              return 0;
            return int(st)
        else:
            st = "".join(tempArr)
            if (int(st) >= pow(2, 31)):
              return 0;
            return int(st)

s = Solution()

s.reverse(123)
