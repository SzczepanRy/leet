class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """



        def merge(arr, B , p ,q , r):
            i = p
            j = q
            k = p
            while i < q and  j < r:

                if arr[i]<=arr[j]:
                    B[k] = arr[i]
                    i+=1
                else:
                    B[k] = arr[j]
                    j+=1
                k+=1

            while i < q :
                B[k] = arr[i]
                k+=1
                i+=1

            while j < r :
                B[k] = arr[j]
                k+=1
                j+=1

            arr[p:r] = B[p:r]

        def msor(arr, B , p ,r):
            if r-p <=1:
                return

            mid = (p+r)//2
            msor(arr,B , p , mid )
            msor(arr,B , mid  , r)
            merge(arr, B, p , mid , r)

        B =[0] * len(nums)
        msor(nums , B , 0 , len(nums) )

        mid = (len(nums)+1)//2

        smaller = nums[:mid]
        bigger= nums[mid:]
        res = [0] * len(nums)

        # Pointer for the end of each half
        s_ptr = len(smaller) - 1
        b_ptr = len(bigger) - 1

        for i in range(len(nums)):
            if i % 2 == 0:
                # Fill even indices with the 'smaller' half from right to left
                B[i] = smaller[s_ptr]
                s_ptr -= 1
            else:
                # Fill odd indices with the 'bigger' half from right to left
                B[i] = bigger[b_ptr]
                b_ptr -= 1
        nums[:] = res
        print(B)





nums = [1,1,2,1,2,2,1]
s = Solution()
print(s.wiggleSort(nums))
