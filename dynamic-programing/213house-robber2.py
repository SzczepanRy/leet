class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        n = len(nums)

        # i dont take last house
        dp = [0]*(n)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(1,n-1):
            dp[i] = max(dp[i-2] + nums[i] , dp[i-1] )

        print(dp)
        m1 = dp[n-2]
        print(m1)



        # i take last house
        dp = [0]*(n)
        dp[0] = 0
        dp[1] = nums[1]
        for i in range(2,n):
            dp[i] = max(dp[i-2] + nums[i] , dp[i-1] )

        print(dp)
        m2 = dp[-1]
        print(m2)


        return max(m2 ,m1)


nums = [1,1]
s= Solution()
print(s.rob(nums))
