class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        n = len(ratings)
        if n == 0:
            return 0

        cukierki = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                cukierki[i] = cukierki[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                cukierki[i] = max(cukierki[i], cukierki[i + 1] + 1)

        return sum(cukierki)

ratings = [29,51,87,87,72,12]
s = Solution()
print(s.candy(ratings))
