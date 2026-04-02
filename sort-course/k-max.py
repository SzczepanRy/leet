class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def parent(i): return (i -1)//2
        def left(i): return i*2 +1
        def right(i): return i*2 +2

        def minheap(arr, i , n):
            #up
            mini = i
            li = left(i)
            ri = right(i)

            if li < n and arr[mini] > arr[li]:
                mini = li

            if ri < n and arr[mini] > arr[ri]:
                mini = ri

            if i != mini :
                arr[mini] , arr[i] = arr[i] , arr[mini]
                minheap(arr, mini, n)

        def buildheap(arr):
            for i in range(len(arr)//2 -1 , -1,-1):
                minheap(arr, i , len(arr))

        arr = nums[:k]

        buildheap(arr)

        for i in range(k , len(nums)):
            num = nums[i]
            if num > arr[0]:
                arr[0] = num
                minheap(arr, 0 , len(arr))

        return arr[0]






s= Solution()
s.findKthLargest([3,2,1,5,6,4] , 2 )
