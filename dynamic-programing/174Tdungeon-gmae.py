class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        n = len(dungeon)
        m = len(dungeon[0])

        # Tworzymy tablicę DP wypełnioną nieskończonością
        # Rozmiar n+1 x m+1 ułatwia obsługę brzegów
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

        # Baza: Aby przeżyć po wyjściu z lochu, potrzebujemy min. 1 HP
        dp[n][m-1] = 1
        dp[n-1][m] = 1

        # Idziemy od prawego dolnego rogu do lewego górnego
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # Ile HP potrzebujemy, żeby wejść tutaj?
                # Wybieramy mniejszą z dróg wyjścia (dół lub prawo)
                needed = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]

                # Jeśli dungeon[i][j] daje dużo HP, 'needed' może być <= 0,
                # ale zawsze musimy mieć min. 1 HP, żeby żyć.
                dp[i][j] = max(1, needed)

        for arr in dp:
            print(arr)

        return dp[0][0]


dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
s = Solution()
print(s.calculateMinimumHP(dungeon))
