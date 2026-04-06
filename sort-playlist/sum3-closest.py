class Solution(object):
    def threeSumClosest(self, nums , target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        #quicksort

        def part(arr, p ,r ):
            fi , li , mi = p , r, (p+r)//2
            f , l , mid = arr[fi] ,arr[li] ,arr[mi]

            pi = 0
            if (f<= mid <= l) or (l <= mid <= f):
                pi = mi
            elif(mid <=f <= l) or (l <= f <= mid):
                pi= fi
            else:
                pi = li

            x = arr[pi]
            arr[r] , arr[pi] = arr[pi] , arr[r]

            i = p -1

            for j in range(p,r):
                if arr[j] <= x:
                    i+=1
                    arr[i] , arr[j] = arr[j] , arr[i]

            arr[i+1] , arr[r] = arr[r] , arr[i+1]
            return i+1

        def qsort(arr, p , r):
            stack = [(p ,r)]
            while len(stack) != 0:
                first , last = stack.pop()
                if first < last:
                    q = part(arr, first, last)

                    stack.append((first,q-1))
                    stack.append((q+1 , last))



        qsort(nums, 0 , len(nums)-1)

        print(nums)




        best= 0
        smallestDiff = float("inf")

        for i in range(len(nums)-2):
            num = nums[i]
            li = i+1
            ri= len(nums)-1

            while li < ri:
                suma = num + nums[li] + nums[ri]

                if abs(suma -target) < smallestDiff:
                    best = suma
                    smallestDiff=abs(suma-target)

                if target > suma:
                    li +=1
                elif target<suma:
                    ri-=1
                else:
                    return target

        print(best)
        return best




nums = [-1,2,1,-4]
target = 1

s= Solution()
s.threeSumClosest(nums , target)
