class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        n = len(nums)

        nums = [1]+nums+[1]

        memo = {}

        def rekur(curr , i , j ):

            if i >j   :
                return 0

            if (i , j ) in memo:
                return memo[(i,j)]

            m = 0

            for k in range(i , j +1):

                ##musze po lewej i po prawej ?
                a = curr[i-1]
                b = curr[k]
                c = curr[j+1]

                val = a*b*c

                m = max( m ,   val + rekur( curr , i , k-1 ) + rekur( curr , k+1 , j ))

            memo[(i,j)] = m
            return m

        return rekur( nums , 1 , n)


nums = [3,1,5,8]

s = Solution()
print(s.maxCoins(nums))
