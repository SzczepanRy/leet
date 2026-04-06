class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """




        def parent(i): return (i-1)//2
        def left(i): return i*2 +1
        def right(i): return i*2 +2

        def heapify(arr , i  , n ):

            maxi = i
            li = left(i)
            ri = right(i)

            if li < n and  arr[li] > arr[maxi]:
                maxi = li
            if ri < n and  arr[ri] > arr[maxi]:
                maxi = ri
            if  maxi != i :
                arr[i] , arr[maxi] = arr[maxi] , arr[i]
                heapify(arr, maxi , n)

        def buildheap(arr):
            n = len(arr)
            for i in range((n//2) -1 , -1 , -1 ):
                heapify(arr,  i , n )

        def hsort(arr):
            buildheap(arr )
            n = len(arr)
            for i in range(n-1, 0,-1):
                arr[0] , arr[i] = arr[i] , arr[0]
                heapify(arr, 0,i )

        hsort(nums)


        counts = [0]*(len(nums))
        counts[0]=1

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                counts[i] = counts[i-1]+1
            else:
                counts[i] =1


        maxc = max(counts)
        if maxc <= len(nums)//3:
            return []

        else:
            res = []
            for i in range(len(counts)):
                if counts[i] > len(nums) //3 and nums[i] not in res :
                    res.append(nums[i])

            return res








nums = [1,2,3]
s = Solution()
s.majorityElement(nums)
