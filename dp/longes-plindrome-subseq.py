# litery długocci jeden zawszwe są palindormami
# spoardzam okienka of i do j ,
# 1) jeśli si == sj to m wimpy że masz ostatni palindorm s[i-1:j-1] został zydłurzony o 2
# 2) jeśli si!= sj to przepisujemy dłudość , albo bez si , olbo bez sj w zalerzność która wieksza

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Tworzymy tablicę n x n wypełnioną zerami
        dp = [[0] * n for _ in range(n)]

        # Każdy pojedynczy znak jest palindromem o długości 1
        for i in range(n):
            dp[i][i] = 1

        # Przechodzimy po długościach podciągów od 2 do n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    # Jeśli znaki na krańcach są takie same, dodajemy 2 do
                    # wyniku dla środka (i+1, j-1)
                    if length == 2:
                        print("len 2 " , s[i:j+1])
                        dp[i][j] = 2
                    else:

                        print("len " , s[i:j+1])
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Jeśli są różne, bierzemy maksimum z dwóch opcji:
                    # 1. Pominiecie lewego znaku (i+1)
                    # 2. Pominięcie prawego znaku (j-1)
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
s = Solution()
print(s.longestPalindromeSubseq("abaaca"))
