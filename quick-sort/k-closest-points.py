class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        for i in points:
            i.append(((i[0])**2 +( i[1])**2))

        print(points)

        def part(arr , p , r):

            fi , li , mi = p , r , (p+r)//2
            f , l , mid = arr[p][2] , arr[r][2] , arr[mi][2]


            pi = -1
            if (f <= mid <= l ) or (l <= mid <= f ):
                pi = mi
            elif (f <= l<= mid ) or (mid <= l <= f ):
                pi =li
            else:
                pi = fi

            x = arr[pi][2]
            arr[pi] , arr[r] =  arr[r] ,arr[pi]

            i = p -1
            for j in range(p ,r):
                if arr[j][2] <= x:
                    i+=1
                    arr[i] , arr[j] = arr[j]  ,arr[i]

            arr[i+1] , arr[r] = arr[r]  ,arr[i+1]
            return i+1


        def k_max(arr , p , r, k):

            if r - p >0:

                q = part(arr, p ,r)

                if q == k:
                    print("good")
                    return arr[0:k+1]
                elif q > k:
                    return k_max(arr , p , q-1 , k )
                else:
                    return k_max(arr ,   q+1 ,r , k )

            return arr[:r+1]
        p = 0
        r = len(points)-1
        res = k_max(points, p , r,k-1)

        print(res)
        for i in res:
            i.pop()

        print(res)
        return res




points =[[1,3],[-2,2],[2,-2]]
k = 2
s = Solution()
s.kClosest(points,k)
