class Solution(object):

    def check(self, jumps , lastI, arr):
        jumps -=1
        lastV = arr[lastI]
        print("arr from " ,lastI , lastI+lastV )
        print(jumps , lastV,  arr[lastI+1:lastI + lastV+1])
        if(jumps == -1 ):
            return False
        maxV = -1
        maxI = 0
        for i in range(lastI+1,len(arr[: lastI+ lastV+1])):

            if(maxV <= arr[i] and arr[i] != 0):
                maxV = arr[i]
                maxI = i

        print("next i ", lastI + maxI )

        if(lastI + maxV > len(arr) or maxI == len(arr)-1 ):
            return True

        return self.check(jumps, maxI , arr)



    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1):
            return 0
        if(nums[0] >= len(nums)-1):
            return 1
        for i in range(1,len(nums)):
            print(self.check(i,0,nums))
            if(self.check(i, 0 , nums)):
                print(i)
                return i



s = Solution()
s.jump([5,9,3,2,1,0,2,3,3,1,0,0])
