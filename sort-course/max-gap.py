class Solution(object):
    def maximumGap(self, nums):

        if len(nums)< 2:
            return 0
        n = len(nums)

        maxn = max(nums)
        x = 1

        while maxn // x > 0:
            buckets = [[] for _ in range(10)]

            for val in nums:
                digit=(val//x)%10
                buckets[digit].append(val)

            nums = []

            for arr in buckets:
                nums.extend(arr)
            x*=10

        maxdiff = 0

        for i in range(1, n):
            maxdiff = max(maxdiff , nums[i] - nums[i-1])

        return maxdiff

nums = [3,6,9,1]
s = Solution()
s.maximumGap(nums)

