from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        l = 0
        max_sum = 0
        current = 0

        for r in range(len(nums)):
            while nums[r] in seen or (r - l + 1 > k):
                current -= nums[l]
                seen.remove(nums[l])
                l += 1

            seen.add(nums[r])
            current += nums[r]

            if r - l + 1 == k:
                max_sum = max(max_sum, current)

        return max_sum