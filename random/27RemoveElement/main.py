class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
       # nums without val
       # k num of val accurences
        lastVal=[]
        lastValIndex=0

        k=0
        for i in range(len(nums)):
            if(nums[i]==val):
                for j in range(i , len(nums)):
                       if(nums[j] != val):
                            nums[i] = nums[j]
                            nums[j] = val
                            break

        for i in nums:
            if(i != val):
                k+=1
        return k
        print(nums,k)


s = Solution()
s.removeElement([0,1,2,2,3,0,4,2] , 2)


