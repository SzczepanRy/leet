class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        max_sum = -float('inf')

        for x in nums:
            # Decyzja: czy dołączyć x do poprzedniej sumy,
            # czy x jest tak duży, że lepiej zacząć od nowa?
            current_sum = max(x, current_sum + x)

            # Sprawdzamy, czy mamy nowy rekord wszech czasów
            max_sum = max(max_sum, current_sum)

        return max_sum

s= Solution()
s.maxSubArray([-2,-1])
