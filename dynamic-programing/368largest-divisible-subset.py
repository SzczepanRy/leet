class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        nums.sort()

        dp = [1]*n ## wielkość największego prawidłego podzbioru kończącego sie na liczbe num[i]
        parent = [-1]*n


        mval= -1
        mind = -1
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[j]+1 > dp[i]:
                    dp[i]= dp[j]+1
                    parent[i]= j

            if dp[i] > mval:
                mval = dp[i]
                mind = i


        res = []
        c = mind
        while c != -1:
            res.append(nums[c])
            c = parent[c]

        return res[::-1]









nums = [1,3,4,8]
s=Solution()
s.largestDivisibleSubset(nums)
