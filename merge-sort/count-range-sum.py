#tablica , z summami , merge , s(i,j) = p[j] - p[i-1]
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """


        # part sum is a o(n) operation
        """

        n = len(nums)
        sums = [0]*n
        sums[0] =nums[0]

        for i in range(1,n):
            sums[i]= sums[i-1]+nums[i]

        result = 0
        for i in range(n):
            for j in range(n-i):
                if i+j == i:
                    if sums[i]>= lower and sums[i] <= upper:
                        result+=1
                else:
                    delta = sums[i+j] - sums[i]
                    if delta>= lower and delta <= upper:
                        result+=1

        print(result)
        return result
        """

        n = len(nums)
        sums = [0]*n
        sums[0] =nums[0]

        for i in range(1,n):
            sums[i]= sums[i-1]+nums[i]

        def mergeSums( p,r) :

            if p-r <=1:
                return 0

            mid = (p+r)//2

            count = mergeSums(p,mid) + mergeSums(mid,r)

            j = k = mid

            for i in range(p,mid):

                while j < r and sums[j]- sums[i] < lower:
                    j+=1

                while k < r  and sums[j]- sums[i] <=higher:


                count += (k-j)


            prefix_sums[p:r] = sorted(prefix_sums[p:r])
            return count





        print(mergeSums(0 n))










nums = [-2,5,-1]
lower = -2
upper = 2

s = Solution()
s.countRangeSum(nums , lower, upper)
