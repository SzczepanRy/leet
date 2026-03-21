class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        if len(citations) == 0:
            return 0



        def merge(arr , B, p , q ,r ):

            i = p
            j = q+1
            k = p

            while i <= p and j <= r:
                if arr[i] > arr[j]:
                    B[k] = arr[i]
                    i+=1
                    k+=1
                else:
                    B[k] = arr[j]
                    j+=1
                    k+=1

            while i <= q:
                B[k]= arr[i]
                k+=1
                i+=1

            while j <= r:
                B[k]= arr[j]
                k+=1
                j+=1

            for ind in range(p,r+1):
                arr[ind]=B[ind]


        def msort(arr,B, p,r):

            if p <r :
                mid = (p+r)//2
                msort(arr,B, p , mid)
                msort(arr, B , mid+1 , r)
                merge(arr , B , p ,mid, r)



        n = len(citations)
        B = [0]*n
        if n > 1:
            msort(citations, B, 0 , n-1)
            citations = B


        print(B)

        i =0
        while citations[i] > i :
            i+=1
            if i > len(citations)-1:

                print(i)
                return i

        print(i)
        return i

citations = [1]

s = Solution()
s.hIndex(citations)



