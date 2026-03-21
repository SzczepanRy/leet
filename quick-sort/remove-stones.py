class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """

        def parent(i): return (i-1)//2
        def left(i): return i*2 +1
        def right(i): return i*2 +2

        def heapifyup_rekur(arr , i,n):

            maxi = i

            li = left(i)
            ri = right(i)

            if li < n and arr[li] > arr[maxi]:
                maxi = li
            if ri < n and arr[ri] > arr[maxi]:
                maxi = ri
            if i != maxi:
                arr[i] , arr[maxi] = arr[maxi], arr[i]
                heapifyup( arr , maxi , n)

        def heapifyup(arr , i,n):
            while True:
                maxi = i
                li = i * 2 + 1
                ri = i * 2 + 2

                if li < n and arr[li] > arr[maxi]:
                    maxi = li
                if ri < n and arr[ri] > arr[maxi]:
                    maxi = ri

                if i != maxi:
                    arr[i], arr[maxi] = arr[maxi], arr[i]
                    i = maxi  # Przechodzimy niżej w pętli
                else:

                    break


        def buildheap(arr):
            n = len(arr)

            for i in range((n//2)-1 ,-1,-1):
                heapifyup(arr, i , n)


        buildheap(piles)


        n = len(piles)
        print(piles)
        for a in range(k):
            maxv = piles[0]//2
            piles[0] -= maxv
            heapifyup(piles, 0 ,n )
            print(piles)


        total=0
        for i in piles:
            total+=i
        print(total)
        return total








piles =[4122,9928,3477,9942]
k = 6

s = Solution()
s.minStoneSum(piles , k)
