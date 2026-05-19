class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        def f(i , L ):

            s = 0
            while L > 0 :
                s += nums[i]*(n-L)
                i = (i+1)%n
                L-=1
            return s



        res=-float("inf")
        for i in range( n ):
            res = max(res , f(i ,n))
        return res

nums = [4,3,2,6]
s=Solution()
print(s.maxRotateFunction(nums))
