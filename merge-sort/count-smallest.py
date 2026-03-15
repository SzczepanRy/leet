class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        dp = [0]*n
        indexes = list(range(n))


        def merge(A, p , q, r,dp , indexes):
            temp_ind= []
            i = p
            j = q
            right_count = 0

            print("merge" ,A ,dp)

            while i < q and j < r :
                if A[indexes[j]] < A[indexes[i]]:
                    temp_ind.append(indexes[j])
                    right_count+=1
                    j+=1

                else:
                    dp[indexes[i]] += right_count
                    temp_ind.append(indexes[i])
                    i+=1

            # clen left
            while i<q:
                dp[indexes[i]]+=right_count
                temp_ind.append(indexes[i])
                i+=1
            # clean right
            while j < r:
                temp_ind.append(indexes[j])
                j+=1

            # update indexes arrat for the segment
            indexes[p:r]=temp_ind

            # i dont knoww

        def mergeSort(A, p ,r,dp , indexes):
            if r-p >1:
                q = (r+p)//2
                mergeSort(A , p, q , dp, indexes)
                mergeSort(A , q, r , dp, indexes)
                merge(A, p, q ,r,dp, indexes)


        mergeSort(nums,0,n,dp , indexes)
        print(dp)

        return dp
        """
        n = len(nums)
        dp = [0]*n
        for i in range(n):
            for j in range(i,n):
                if nums[i] > nums[j]:
                    dp[i]+=1

        return dp
        """

nums = [5,2,6,1]
s = Solution()
s.countSmaller(nums)



