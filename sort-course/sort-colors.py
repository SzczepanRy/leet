

class Solution(object):
    def sortColors(self, nums):

        A = [0] *( max(nums)+1)
        B = [0] *(len(A))

        for i in nums:
            A[i]+=1


        for i in range(1,len(A)):
            B[i] = B[i-1] + A[i-1]

        sorted = [0]*len(nums)
        for i in nums:
            sorted[B[i]]= i
            B[i]+=1

        nums[:] = sorted[:]

s = Solution()
s.sortColors([2,0,2,1,1,0])
