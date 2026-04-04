
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """


        if len(nums) == 1:
            return nums

        minn = min(nums)
        nums = [num - minn  for num in nums]


        maxn = max(nums)
        minnew = min(nums)

        bucketnum =int((maxn)**(1/2))

        size = maxn//bucketnum



        buckets = [[] for _ in range(bucketnum)]

        for val in nums:
            index = ((val - minnew) *(bucketnum-1))//(maxn - minnew)
            buckets[index].append(val)


        print(buckets)


        #quickselect on buckets len


        def getfreq(arr):
            # small numbers count sort good
            min2 = min(arr)
            arr = [num - min2 for num in arr]
            max2 = max(arr)
            count = [0]*(max2+1)

            for val in arr:
                count[val]+=1

            res = []
            for i , val in enumerate(count):

                l = 0
                r = len(res)
                while l < r:
                    mid = (l+r)//2
                    if res[mid][1] < val :
                        r= mid -1
                    else:
                        l = mid +1

                # questionable
                res.insert(l , [i +1+ min2 , val])

            return res

        def part(arr , p , r ):

            fi , li  , mi =  p , r , (p+r)//2
            f , l , mid = len(arr[fi]) , len(arr[li]) , len(arr[mi])

            pi= 0
            if (l <= mid <= f) or (f <= mid <= l ):
                pi = mi
            elif ( f<= l <= mid ) or (mid <= l <= f):
                pi = li
            else:
                pi = fi

            x=len(arr[pi])

            arr[pi] , arr[r] = arr[r] , arr[pi]

            i = p-1

            for j in range(p ,r):
                if len(arr[j]) >= x:
                    i+=1
                    arr[j] , arr[i] = arr[i] , arr[j]


            arr[r] , arr[i+1] = arr[i+1] , arr[r]
            return i+1

        def qsel(arr , p ,r, k ):
            if p <r:
                q= part(arr , p ,r)
                if k == q:
                    return arr[p : k]
                elif q < k:
                    return qsel(arr, q+1 , r ,k)
                else:
                    return qsel(arr, p , q-1 ,k)

            return arr[:p]

        def merge(arr1, arr2):

            result = []
            i = 0
            j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i][1] > arr2[j][1]:
                    result.append(arr1[i])
                    i+=1
                else:
                    result.append(arr2[j])
                    j+=1

            result.extend(arr1[i:])
            result.extend(arr2[j:])
            return result



        if len(buckets) != 1:
            res = qsel(buckets , 0 , len(buckets)-1,k)
            freq_lists = [getfreq(b) for b in res if b]

            while len(freq_lists) > 1:
                next_round = []
                for i in range(0, len(freq_lists), 2):
                    if i + 1 < len(freq_lists):
                        # Merge two frequency lists
                        next_round.append(merge(freq_lists[i], freq_lists[i+1]))
                    else:
                        # Keep the odd one for the next round
                        next_round.append(freq_lists[i])
                freq_lists = next_round

            final_res = freq_lists[0]

        else:
            result=[]
            res = getfreq(buckets[0])
            for i in range(k):
                result.append(res[i][0])
            res = [n - minn  for n in result ]
            print(res)
            return res





nums = [1,2,1,20,20,20,20,20,10,10,1,2,2,3,3,3,2]
k = 2

s = Solution()
s.topKFrequent(nums , k)
