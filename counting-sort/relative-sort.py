class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """


        maxn = max(arr1)
        count = [0]*(maxn+1)


        for num in arr1:
            count[num]+=1

        res = []

        for num in arr2:
            while count[num] > 0 :
                res.append(num)
                count[num]-=1

        for num in  range(len(count)):
            while count[num] > 0 :
                res.append(num)
                count[num]-=1

        return res






s = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
s.relativeSortArray(arr1,arr2)
