
class Solution(object):

    def longestSubsequence(self, arr, difference):
        dp = {} # liczba -> max długość ciągu

        for x in arr:
            # Sprawdzamy, czy istnieje liczba, która mogłaby być przed 'x'
            # x - prev = difference  =>  prev = x - difference
            prev = x - difference

            if prev in dp:
                dp[x] = dp[prev] + 1
            else:
                dp[x] = 1
        print(dp)
        return max(dp.values())

arr = [1,5,7,8,5,3,4,2,1]
difference = -2
s= Solution()
s.longestSubsequence(arr , difference)

"""
my solution , good but slow
class Solution(object):

    def longestSubsequence(self, arr, difference):
        n = len(arr)
        dp = [1]*n
        for i in range(1,n):
            for j in range(i):

                if arr[j] + difference == arr[i]:
                    dp[i] = max(dp[i] , dp[j]+1)

        print(dp)
        return max(dp)

arr = [1,3,5,7]
arr = [1,5,7,8,5,3,4,2,1]
difference = -2
s= Solution()
s.longestSubsequence(arr , difference)

"""
