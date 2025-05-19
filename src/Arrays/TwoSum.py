class Solution:
    def TwoSum(self, nums: list[int], target: int) -> list[int]:
        comp = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in comp:
                return [comp[complement], i]
            comp[num] = i

        return [0, 0]