class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        memo= {}

        def rekur(r):
            if r < 0 :
                return float("inf")
            if r == 0 :
                return 0
            if r in memo:
                return memo[r]

            res= float("inf")

            for c in coins:
                sub_res = rekur(r-c)
                if sub_res != float("inf"):
                    res = min(res, sub_res+1)

            memo[r] = res
            return res

        res = rekur(amount)

        if res == float("inf"):
            return -1
        return res

coins = [1,2,5]
amount = 11
s= Solution()
s.coinChange(coins,amount)



