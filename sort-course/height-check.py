class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def parent(i): return (i-1)//2;
        def left(i): return i*2+1;
        def right(i): return i*2 +2;

        def heapify(arr , i, n ):

            mini = i
            li = left(i)
            ri = right(i)

            if li < n and arr[li] < arr[mini]:
                mini = li
            if ri < n and arr[ri] < arr[mini]:
                mini = ri
            if mini!= i:
                arr[mini] , arr[i] = arr[i] , arr[mini]
                heapify(arr, mini, n)

        def buildheap(arr ):
            n = len(arr)
            for i in range(n-1 , -1 ,-1):
                heapify(arr, i,n)

        def heapsort(arr):
            buildheap(arr)
            n = len(arr)
            res = [0]*n
            inf = float("inf")
            for i in range(len(arr)):
                res[i] = arr[0]
                arr[0] = inf
                heapify(arr, 0 , n)
            return res

        heights_cp = heights[:]
        res = heapsort(heights)
        result = 0
        for  i in range(len(res)):
            if res[i] != heights_cp[i]:
                result+=1

        print(result)
        return result


s = Solution()
heights = [1,1,4,2,1,3]
s.heightChecker(heights)
