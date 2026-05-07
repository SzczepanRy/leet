class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        initial = list(s)
        dp = [initial]

        def isPal(s):

            for i in range(len(s)//2):
                if s[i] != s[len(s)-1-i] :
                    return False

            return True


        i = 0
        while i < len(dp):

            for j in range(2 , len(dp[i])):


                #j size of window
                print(j)

                for k in range(j , len(dp[i])+1):
                    if j ==3:
                        print(dp[i][k-j : k])

                    st = "".join(dp[i][k-j : k])

                    if isPal( st) :
                        tmp = dp[i][:k-j]
                        tmp.append(st)
                        tmp.extend(dp[i][k:])
                        dp.append(tmp)
                        print(tmp)



            i+=1


        print(dp)









st = "aaba"
s= Solution()
s.partition(st)
