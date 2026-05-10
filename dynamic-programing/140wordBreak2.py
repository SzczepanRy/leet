class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        n = len(s)

        dp = [[]for _ in range(n+1)]

        lastind = [0]
        while lastind:
            last = lastind.pop()

            for i in range(last+1,n+1):

                if s[last:i] in wordDict:
                    dp[i].append((last, s[last:i]))

                    lastind.append(i)



        print(dp)

        res = []

        def rekur(currArr , ind ):
            if ind == 0 :
                print(currArr)
                t = currArr[::-1]
                string = " ".join(t)
                if string not in res:

                    res.append(string)
                return


            """
            while dp[ind]:
                tup=dp[ind].pop()
                currArr.append(tup[1])
                rekur(currArr, tup[0])
                currArr.pop()


            """
            for tup in dp[ind]:
                currArr.append(tup[1])

                rekur(currArr, tup[0])
                currArr.pop()



        rekur([], n)

        print(res)

        return res



s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

sol = Solution()
sol.wordBreak(s , wordDict)
