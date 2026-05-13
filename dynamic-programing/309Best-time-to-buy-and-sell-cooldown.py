class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """


        memo = {}

        def rekur(i , czy_trzymam ):

            if i >= len(prices) :
                return 0

            state = (i , czy_trzymam)
            if state in memo:
                return memo[state]

            wyniki = 0
            if czy_trzymam:
                # sprzedaje  i lece i+2
                sprzedaje = rekur( i +2 , False )+  prices[i]
                czekam = rekur(i+1 , True )
                wyniki = max(sprzedaje ,czekam )

            else:
                kupuje = rekur(i +1 , True )  -prices[i]
                czekam = rekur(i +1 , False )

                wyniki = max(kupuje,czekam )

            memo[state] = wyniki
            return wyniki



        return rekur(0 , False )


prices = [2,4,0,3,0,2]
s=Solution()
print(s.maxProfit(prices))
