import math
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            # Musimy zapisać curMax w tymczasowej zmiennej,
            # bo zaraz go zmienimy, a będzie potrzebny do curMin
            tempMax = curMax * n

            # Kluczowy moment: sprawdzamy trzy opcje:
            # 1. Sama obecna liczba (zaczynamy od nowa)
            # 2. Obecna liczba * poprzedni max
            # 3. Obecna liczba * poprzedni min (minus * minus = plus!)
            curMax = max(n, tempMax, curMin * n)
            curMin = min(n, tempMax, curMin * n)

            res = max(res, curMax)

        return res
nums = [2,3,-2,21 , -20,4]
s = Solution()
print(s.maxProduct(nums))
