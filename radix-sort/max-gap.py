class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n < 2 :
            return 0


        x = 1
        m =max(nums)
        while m // x >0 :

            buckets = [[] for _ in range(10)]

            for val in nums:
                d = (val//x)%10
                buckets[d].append(val)

            nums = []

            for arr in buckets:
                nums.extend(arr)

            x*=10


        maxdiff = 0
        for i in range(1,n):
            maxdiff = max(maxdiff , nums[i]- nums[i-1] )

        return maxdiff






nums = [3,6,9,1]
s = Solution()
s.maximumGap(nums)
