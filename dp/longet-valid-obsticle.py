class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """

        """
        moje za wolne
        n = len(obstacles)
        dp=[1]*n

        for i in range(1,n):
            for j in range(i):
                if obstacles[i] - obstacles[j]>=0 :
                    dp[i] = max(dp[i] , dp[j]+1)
        print(dp)
        return dp
        """

    n = len(obstacles)
    ans = [0] * n
    tails = []

    for i in range(n):
        height = obstacles[i]

        # Własna implementacja bisect_right
        # Szukamy najmniejszego elementu w tails, który jest ŚCIŚLE WIĘKSZY od height
        low = 0
        high = len(tails)

        while low < high:
            mid = (low + high) // 2
            if tails[mid] <= height:
                low = mid + 1
            else:
                high = mid

        idx = low

        # Jeśli nie znaleźliśmy większego elementu, wysokość wydłuża nasz najdłuższy ciąg
        if idx == len(tails):
            tails.append(height)
        else:
            # W przeciwnym razie aktualizujemy tails, by zachować najniższą możliwą
            # wartość dla tej długości ciągu (to pozwala na łatwiejsze dołączanie w przyszłości)
            tails[idx] = height

        ans[i] = idx + 1

    return ans



obstacles = [3,1,5,6,4,2]
s=Solution()
s.longestObstacleCourseAtEachPosition(obstacles)
