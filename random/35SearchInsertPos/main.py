class Solution(object):


    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        print(target)

        if( target <= nums[0]):
            return 0
        if( target > nums[len(nums)-1]):
            return len(nums)

        for i in range(len(nums)):
            if( nums[i] >=target ):
                print(i)
                return i




s= Solution()

s.searchInsert([1,2,3,3,4,5] , 3)


