class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = list(set(nums))
        arr.sort()
        k= len(arr)
        for i in range(len(arr)):
            nums[i] = arr[i]

        return k

s = Solution()
s.removeDuplicates([-1,0,0,0,0,3,3])
