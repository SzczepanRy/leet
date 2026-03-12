class Solution:
    def deleteAndEarn(self, nums) :

        if not nums:
            return 0

        # 1. Find the range we need for our "street"
        max_val = max(nums)

        # 2. Transform into a House Robber problem
        # Each index i will store the total points possible from value i
        buckets = [0] * (max_val + 1)
        for x in nums:
            buckets[x] += x

        # 3. Apply the House Robber DP logic
        prev2, prev1 = 0, 0
        for points in buckets:
            # Standard DP: max(skip current, rob current + two houses ago)
            temp = max(prev1, points + prev2)
            prev2 = prev1
            prev1 = temp

        return prev1
s = Solution()
print(s.deleteAndEarn([3,4,2]))
print(s.deleteAndEarn([2,2,3,3,3,4]))


