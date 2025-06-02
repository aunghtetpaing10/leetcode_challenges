class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums) - 1):
            num1 = nums[i]
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                if num1 + num2 == target:
                    return [i, j]