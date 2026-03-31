class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i, e in enumerate(nums):
            if target - e in memo:
                return [memo[target-e], i]
            memo[e] = i        