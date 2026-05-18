class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n=len(nums)
        dp = [1]*n


        last = [0]*n

        for i in range(1,n):
            for j in range(i):
                diff = nums[i] - nums[j]

                if diff != 0:


                        if last[j] >= 0 and diff < 0 :

                            if dp[i] < dp[j]+1:
                                last[i] = diff
                                dp[i] = dp[j]+1



                        elif last[j] <= 0 and diff > 0 :
                            if dp[i] < dp[j]+1:
                                last[i] = diff
                                dp[i] = dp[j]+1




        return max(dp)



nums = [1,7,4,9,2,5]
nums = [1,17,5,10,13,15,10,5,16,8]
s = Solution()
s.wiggleMaxLength(nums)
