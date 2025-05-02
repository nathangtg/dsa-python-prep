class Solution:
    def TwoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [i, hash_map[complement]]
            else:
                hash_map[num] = i

        return  []
