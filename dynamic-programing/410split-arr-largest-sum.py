class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]

        for i in range(1, n ):
            prefix[i] = nums[i] + prefix[i-1]


        dp = [[0]*(k+1) for i in range(n+1)]
        dp[0][0]=0

        # dp i j nim-max suma dla i elementów  oraz j podziałów
        print(nums)
        print(prefix)

        for j in range(1, k +1):




nums = [7,2,5,10,8]
k = 2
s = Solution()
s.splitArray(nums, k)
