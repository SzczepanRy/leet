class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = [0] * (n+1)

        for i in range(1 , n+1):
            c = i%2
            o = i//2


            if i-o >= 0 :
                print( i ,c , o  ,arr[i-o])
                arr[i] = arr[i - o -c] + c

        return arr


s=Solution()
s.countBits(5)
