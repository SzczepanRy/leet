class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)


        mright = [0]*n
        mright[0] = height[0]
        for i in range(1,len(height)):
            mright[i] = max(height[i] ,mright[i-1] )

        mleft= [0]*n
        mleft[-1] = height[-1]

        for i  in range(len(height)-2 ,-1 ,-1):
            mleft[i] = max(height[i] ,mleft[i+1] )

        count = 0
        for i in range(len(height)):
            count += max(0 , min(mleft[i] , mright[i])- height[i])

        return count



s=Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
