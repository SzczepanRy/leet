
# najkrousza scierzka po skoku jeden lub dwa
#greedy algorithm

class Solution:
    def minCostClimbingStairs(self, cost) :
        # dp[i] to minimalny koszt wejścia na stopień i
        # Możemy zacząć od stopnia 0 lub 1 (koszt początkowy 0)

        # Koszt dotarcia do stopnia 0 i 1 wynosi 0
        a, b = 0, 0

        for i in range(2, len(cost) + 1):
            # Obliczamy koszt dla bieżącego stopnia
            # Musimy dodać koszt stopnia, z którego skaczemy
            current_cost = min(a + cost[i-2], b + cost[i-1])

            # Przesuwamy okno
            a = b
            b = current_cost

        return b


s = Solution()
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
'''
a b
0 0 (1 ,100)=>1
0 1 (100 , 2)=>2
1 2 (2,3)=>2
2 2 (3,3) =>3
2 3 (3 ,103) =>3
3 3 (103 , 4) = > 4
3 4 (4,5)=>4
4 4 (5 104)=>5
4 5 (104, 5)=>6
6
'''
