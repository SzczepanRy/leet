# jeze z tych dwuch tmy na domu i , co zanczy ze suma jest rowna i-2 + i lub i-1  wysimy wybrac z tych dwoch
class Solution:
    def rob(self, nums) :

        if not nums:
            return 0

        prev2, prev1 = 0, 0

        for amount in nums:
            temp = max(prev1, amount + prev2)
            prev2 = prev1
            prev1 = temp

        return prev1

s = Solution()
print(s.rob([2,7,9,3,1]))

