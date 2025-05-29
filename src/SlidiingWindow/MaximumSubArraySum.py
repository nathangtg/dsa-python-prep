from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        curr_sum = 0
        max_sum = 0
        l = 0

        for r in range(len(nums)):
            while nums[r] in seen or (r - l + 1 > k):
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l += 1

            seen.add(nums[r])
            curr_sum += nums[r]

            if r - l + 1 == k:
                max_sum = max(curr_sum, max_sum)

        return max_sum