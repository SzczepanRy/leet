class Solution(object):
    def minimumAbsDifference(self, arr):

        def merge(arr,B, p  , q, r ):

            i = p
            j = q
            k = p

            while i < q and j < r:

                if arr[i] < arr[j]:
                    B[k] = arr[i]
                    i+=1
                else:
                    B[k] = arr[j]
                    j+=1

                k+=1

            while i < q :
                B[k]= arr[i]
                k+=1
                i+=1

            while j < r :
                B[k]= arr[j]
                k+=1
                j+=1

            arr[p:r] = B[p:r]


        n = len(arr)
        B=[0]*(n)

        width= 1
        while width < n :
            for p in range(0 , n , width*2):
                mid = min(p+width ,n)
                r = min( p+2*width, n)

                merge(arr,B,p,mid,r)
            width *=2

        diffs = [float("inf")] *n

        ind = 1
        mindiff = float("inf")
        for i in range(0 , n-1):

            a = arr[i]
            b = arr[i+1]
            diff = b-a
            diffs[ind] = diff
            if mindiff>diff:
                mindiff = diff
            ind+=1


        res = []
        for i in range(1,len(diffs)):
            if diffs[i] == mindiff:
                res.append([arr[i-1] , arr[i]])



        return res


arr = [3,8,-10,23,19,-4,-14,27]

s = Solution()
s.minimumAbsDifference(arr)
