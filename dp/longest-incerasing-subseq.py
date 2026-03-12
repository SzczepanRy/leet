class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        n = len(nums)
        # Każda liczba sama w sobie jest podciągiem o długości 1
        dp = [1] * n

        print(nums)
        for i in range(1, n):
            print(i)
            for j in range(i):
                if nums[j] <nums[i]  :
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)



s= Solution()
s.lengthOfLIS([10,9,2,5,3,7,101,18])

