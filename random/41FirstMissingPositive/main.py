class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        nums = list(nums)
        nums.sort()
        numI = 1
        for i in range(len(nums)):
            if( nums[i] > 0 ):
                if nums[i] != numI:

                    print(i, numI , nums[i])
                    return numI
                else :
                    numI+=1
        return numI
s = Solution()

s.firstMissingPositive([0, 1, 1, 2, 2])
