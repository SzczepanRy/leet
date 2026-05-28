class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #art at least 3 els
        n = len(nums)
        dp = [0]*n

        if n <3:
            return 0



        last =float("inf")
        lastind = -1
        count = 1

        for i in range(2 , n):

            if  nums[i-1]*2 == nums[i-2] + nums[i]:
                # mamy cząstke ciągu

                if last == nums[i] - nums[i-1] and lastind == i-1:

                    #jeśli ostatnia reszta była taka sama to mnorzymy ją  przez count (iloe było w ciągu)

                    dp[i] =dp[i-1] + (count +1)
                    count +=1
                    lastind = i

                else:
                    #przerywany ciąg dodajeny tyjko jedno
                    count = 1
                    dp[i]= dp[i-1]+1
                    last = nums[i] - nums[i-1]
                    lastind = i
            else:
                dp[i] = dp[i-1]

        return dp[-1]








nums = [1,2,3,4,4,4]
s = Solution()
s.numberOfArithmeticSlices(nums)
