class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """


        s = sum(nums)

        if  s%2 == 1:
            return False

        exp = (s+1)//2

        dp = [False] * (exp+1)

        dp[0]= True

        for num in nums:
            for t in range(exp , num-1 , -1 ):
                if dp[t - num]:
                    dp[t] = True
        return dp[-1]


        """
        n = len(nums)

        # jeśli id tnieje i ,r jest już obliczone to zwracamy wart , szybie piszt np 10,10,10,10...
        memo = {}

        def rekur(i, r):

            if n == i:
                if r == 0:
                    return True
                else:
                    return False

            if (i,r) in memo:
                return memo[(i,r)]

            w = rekur(i+1 , r+nums[i]) or rekur(i+1,  r - nums[i])

            memo[(i , r)]  = w
            return w

        return rekur(0 , 0)

        """

nums = [1, 5, 11, 5]
s = Solution()
print(s.canPartition(nums))
