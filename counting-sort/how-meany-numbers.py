class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        maxn = max(nums)

        count = [0]*(maxn+1)

        for num in nums:
            count[num]+=1

        res = []

        for num in nums:
            c = 0
            for i in range(num):
                c += count[i]

            res.append(c)

        return res




nums = [8,1,2,2,3]
s = Solution()
s.smallerNumbersThanCurrent(nums)
