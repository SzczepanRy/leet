class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def merge(A ,B , p , q , r):

            i = p
            k = p
            j = q+1

            while i <= q and j <= r:
                if A[i] >= A[j]:
                    B[k] = A[i]
                    i+=1
                else:
                    B[k] = A[j]
                    j+=1

                k+=1

            while i<= q:
                B[k] =A[i]
                k+=1
                i+=1
            while j<= r:
                B[k] =A[j]
                k+=1
                j+=1

            for ind in range(p,r+1):
                A[ind] = B[ind]


        def msort(A,B,p,r):
            if r - p > 0 :
                mid = (p+r)//2
                msort(A,B,p , mid)
                msort(A,B,mid+1 ,r)
                merge(A,B,p,mid,r)


        n = len(nums)
        B = [0]*n
        if n > 1:

            msort(nums, B , 0 , n -1 )
            nums =B
        res = 0

        for i in range(0 , n , 2 ):
            res += min(nums[i] , nums[i+1])


        return res
nums = [6,2,6,5,1,2]
s=Solution()
s.arrayPairSum(nums)


