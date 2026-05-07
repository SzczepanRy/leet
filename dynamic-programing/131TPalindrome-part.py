class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """


        n = len(s)


        # jeśli true w [i][j] to s[i : j+1] jest palindromeme
        dp = [[False]*n for _ in range(n)]



        # n+1 bo jebać indekstownie końcowe
        for length in range(1 , n +1):
            for i in range(n - length+1 ):
                j = length + i -1 # -1 bo chcemy [1][1] ex

                if s[i] == s[j]:
                    # to jest inicjalizacja palindoromy moaą mieś środekk długosci 1 i 2
                    # lub napitkaliśmy środek który dył już palindorameme

                    if length < 3 or dp[i+1][j-1]:
                        dp[i][j] = True


        for arr in dp :
            print(arr)

        res = []

        #dudowanie tabeli , dfs po dp


        def findres(start, currPath):

            if start == n :
                res.append(currPath[:])
                return

            for end in range(start, n ):
                if dp[start][end]:
                    currPath.append(s[start:end+1])
                    findres(end +1 , currPath)
                    currPath.pop()


        findres(0 , [])

        return res











st = "aabaa"
s= Solution()
s.partition(st)
