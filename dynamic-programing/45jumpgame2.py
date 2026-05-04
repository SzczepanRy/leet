class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        memo = [-1]*len(nums)

        def rekur(ind):

            if ind >= len(nums)-1:
                return 0

            if memo[ind] != -1:
                return memo[ind]

            m = float("inf")

            for i in range(1, nums[ind]+1):
                m = min(1+rekur(ind+i), m)

            memo[ind]=m
            return m


        return rekur(0)




s = Solution()
s.jump([2,3,1,1,4])
