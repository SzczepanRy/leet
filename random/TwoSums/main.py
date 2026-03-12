class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range( i, len(nums)):
                if(nums[i]+nums[j] == target and i!=j):
                    return [i,j]

sol= Solution()
print(sol.twoSum([-1,-2,-3,-4,-5],-8))
