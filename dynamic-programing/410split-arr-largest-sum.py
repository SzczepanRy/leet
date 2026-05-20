class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n = len(nums)
        prefix = [0]*(n+1)
        prefix[0] = nums[0]

        for i in range( n ):
            prefix[i+1] = nums[i] + prefix[i]


        dp = [[float("inf")]*(k+1) for i in range(n+1)]
        dp[0][0]=0

        # dp i j nim-max suma dla i elementów  oraz j podziałów
        print(nums)
        print(prefix)

        for j in range(1, k +1):

            for i in range(1, n +1):
                # p to miejsce ostatniego cięcia
                for p in range(j - 1, i):
                    current_sum = prefix[i] - prefix[p]
                    # Szukamy minimum z maksimów
                    res = max(dp[p][j-1], current_sum)
                    dp[i][j] = min(dp[i][j], res)

        for i in dp:
            print(i)

        return dp[n][k]











nums = [7,2,5,10,8]
k = 2
s = Solution()
s.splitArray(nums, k)
