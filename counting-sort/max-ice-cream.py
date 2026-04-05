class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """

        if not costs:
            return 0

        maxn = max(costs)

        counts =[0]*(maxn+1)

        for num in costs:
            counts[num]+=1


        count = 0
        for i in range(len(counts)):
            if counts[i]>0:
                if i == 0:
                    count += counts[i]
                    continue
                while counts[i]>0 and coins>=i:
                    coins-=i
                    count+=1
                    counts[i]-=1


                if counts[i] > 0 and coins < i:
                    break


        return count








costs = [11]
coins = 1

s = Solution()
s.maxIceCream(costs , coins)
