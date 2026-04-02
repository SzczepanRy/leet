class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        """
        arr= nums
        def parent(i): return (i-1)//2
        def left(i): return 2*i +1
        def right(i): return 2*i +2

        def maxheap(arr , i ,n):

            maxi = i

            li = left(i)
            ri = right(i)

            if li<n and arr[maxi] < arr[li]:
                maxi= li
            if ri <n and arr[maxi] < arr[ri]:
                maxi= ri

            if maxi != i:
                arr[maxi] , arr[i] = arr[i] , arr[maxi]
                maxheap(arr, maxi ,n)


        def buildheap(arr):
            for i in range(len(arr)//2  -1 , -1 , -1 ):
                maxheap(arr, i , len(arr))

        def hsort(arr):
            buildheap(arr)
            for i in range(len(arr) -1, 0 , -1 ):
                arr[i], arr[0] = arr[0] , arr[i]
                maxheap(arr, 0 , i )

        hsort(arr)

        return arr

s = Solution()
s.sortArray([5,4,2,67,7,3,22,3,4,5])



