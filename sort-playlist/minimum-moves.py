class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        # 2. Wybieramy medianę
        n = len(nums)
        median = nums[n // 2]

        # 3. Liczymy sumę ruchów
        moves = 0
        for num in nums:
            moves += abs(num - median)

        return moves



s = Solution()
s.minMoves2()
