class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        def part(arr , p ,r ):

            fi , li , mi  = p , r , (p+r)//2
            f , l , mid  = arr[fi] , arr[li] , arr[mi]

            pi = -1
            if ( f<= mid<=l) or (l<=mid<=f):
                pi = mi
            elif (f<= l <= mid) or (mid <= l <= f):
                pi = li
            else:
                pi = fi

            x = arr[pi]
            arr[pi] , arr[r] = arr[r] , arr[pi]

            i = p-1
            for j in range(p ,r ):
                if arr[j] <= x:
                    i+=1
                    arr[i] , arr[j] = arr[j] , arr[i]

            arr[i+1] , arr[r] = arr[r] , arr[i+1]

            return i+1


        def qsortclassic(arr , p , r ):
            if r - p > 0:
                q = part(arr , p , r)
                qsortclassic(arr , p , q -1)
                qsortclassic(arr ,  q +1 , r)

        n = len(arr)
        qsortclassic(arr, 0 , n -1)

        m = arr[(n-1)//2]

        res=[]
        f = 0
        l = n-1
        for i in range(k):
            if abs(arr[f] - m) > abs(arr[l] - m):
                res.append(arr[f])
                f+=1
            else:
                res.append(arr[l])
                l-=1

        print(res)

        return res


arr = [6,7,11,7,6,8]
k = 5


arr = [1,1,3,5,5]
k = 2
s = Solution()
s.getStrongest(arr,k)
