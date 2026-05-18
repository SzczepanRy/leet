class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        """
        #memo = []

        #def rekur(s , curr):
        def rekur(s):
            if s< 0:
                return 0

            if s ==  0:
                #memo.append(curr[:])
                return 1

            #ncurr = curr[:]
            comp = 0
            for z in nums:
                #ncurr.append(z)
                #comp += rekur(s-z , ncurr)
                #ncurr.pop()
                comp += rekur(s-z)

            return comp



        #print(rekur(target, []))
        return rekur(target)

        #print(memo)
        """



        memo = {}

        def rekur(s):
            if s < 0:
                return 0

            if s == 0:
                return 1


            if s in memo:
                return memo[s]

            comp = 0
            for z in nums:
                comp += rekur(s-z)


            memo[s]= comp
            return comp

        return rekur(target)

        #print(memo)




num=[1,2,3]
temp = 4
s = Solution()
s.combinationSum4(num , temp)
