class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """

        starts= []

        for i in  range(len(intervals)):
            starts.append((intervals[i][0] , i ))


        def part(arr,p , r):
            fi , li , mi =  p ,r , (p+r)//2
            f , l  ,mid = arr[fi][0] , arr[li][0] , arr[mi][0]

            pi = -1
            if (f<= mid <= l) or (l <= mid <= f ):
                pi = mi
            elif (f<= l <= mid) or (mid <= l  <= f ):
                pi = li
            else:
                pi = fi

            x = arr[pi]

            arr[pi] , arr[r] = arr[r] , arr[pi]

            i = p-1

            for j in range(p ,r):
                if arr[j][0] <= x[0]:
                    i+=1
                    arr[i] , arr[j] = arr[j] , arr[i]

            arr[i+1] , arr[r] = arr[r] , arr[i+1]

            return i+1

        def qsort(arr,p,r):

            stack = [(p,r)]
            while len(stack) != 0:

                left , right = stack.pop()

                if left <right :
                    mid = (p+r)//2
                    q = part(arr, left , right)
                    stack.append((left , q-1))
                    stack.append((q+1,right))


        qsort(starts, 0 , len(starts)-1)

        res = []
        for i in range(len(intervals)):
            pair=intervals[i]
            end = pair[1]

            l = 0
            r = len(starts)-1
            ind = -1

            while l <=r :
                mid= (l+r)//2
                if starts[mid][0] >= end:
                    ind= starts[mid][1]
                    r = mid -1
                else:
                    l = mid +1

            res.append(ind)

        return res




intervals = [[3,4],[2,3],[1,2]]
s = Solution()
s.findRightInterval(intervals)
