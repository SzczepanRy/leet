class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def maxsub(arr ,x ):
            stack = []
            n= len(arr)
            i = 0
            while i < n :
                while len(stack)!=0 and arr[i] > stack[-1] and len(stack) + n - i > x:
                    stack.pop()

                stack.append(arr[i])
                i+=1

            return stack[:x]


        def merge(arr1, arr2):
            stack = []
            n= len(arr1)
            m= len(arr2)
            i = 0
            j = 0

            while i < n or j < m :


                # ta linijka to look achead
                if arr1[i:] > arr2[j:]:
                    stack.append(arr1[i])
                    i+=1
                else:
                    stack.append(arr2[j])
                    j +=1

            return stack


        res = [-float("inf")]

        start = max(0 , k - len(nums2))
        end= min(k , len(nums1))

        for y in range(start,end+1):
            x = k-y

            arr1 = maxsub(nums1, y)
            arr2 = maxsub(nums2, x)
            r = merge(arr1, arr2)

            if res < r:
                res = r

        return res


nums1 = [3,4,6,5]
nums2 = [9,1,2,5,8,3]
k = 5

s=Solution()
print(s.maxNumber(nums1 , nums2,k))
