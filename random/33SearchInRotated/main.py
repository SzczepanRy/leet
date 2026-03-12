class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        s= set(nums)
        try:
            print(nums.index(target))
            return nums.index(target)
        except:
            print(-1)
            return -1

s = Solution()

s.search([4,5,6,7,0,1,2], 3)
