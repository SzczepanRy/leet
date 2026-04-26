class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_score = [0] * (n + 1)

        for a, b in trust:
            # Osoba 'a' ufa komuś -> tracimy szansę na bycie sędzią
            trust_score[a] -= 1
            # Osoba 'b' jest obdarzona zaufaniem -> zyskuje punkt
            trust_score[b] += 1

        # Szukamy osoby, która ma wynik n - 1
        for i in range(1, n + 1):
            if trust_score[i] == n - 1:
                return i

        return -1




n = 3
trust = [[1,3],[2,3],[3,1]]
s = Solution()
s.findJudge(n, trust)
