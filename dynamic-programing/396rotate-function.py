class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        total_sum = sum(nums)

        # Calculate F(0) initial state
        current_f = sum(i * num for i, num in enumerate(nums))
        max_f = current_f

        # Roll through the array backward to compute consecutive F(i) values
        for i in range(1, n):
            # Using our derived formula:
            current_f = current_f + total_sum - n * nums[n - i]
            max_f = max(max_f, current_f)

        return max_f
