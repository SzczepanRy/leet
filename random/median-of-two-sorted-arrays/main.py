class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        l1 = len(nums1)
        l2 = len(nums2)
        result=[]
        i = 0
        j  = 0
        while (i+j) < (l1 +l2):
            print(i , j , l1 ,l2)

            if(i == l1):
                result.append(nums2[j])
                j+=1
                continue
            if(j == l2):
                result.append(nums1[i])
                i+=1
                continue


            if(nums1[i]<nums2[j]):
                if(i < l1):
                    result.append(nums1[i])
                    i+=1
                    continue
            if(nums1[i]>nums2[j]):
                if(j < l2):
                    result.append(nums2[j])
                    j+=1
                    continue
            else:
                if(j < l2):
                    result.append(nums2[j])
                    j+=1

                if(i < l1):
                    result.append(nums1[i])
                    i+=1

        print(result)
        reslen = len(result)
        if reslen%2 ==1:
            print(result[reslen//2])
            return result[reslen//2]
        else:
            print( ( float(result[(reslen//2)-1 ]) +  float(result[reslen//2]))/2 )

            return  (float(result[(reslen//2)-1 ]) +  float(result[reslen//2]))/2

s = Solution()
s.findMedianSortedArrays([1,3] ,[2])
