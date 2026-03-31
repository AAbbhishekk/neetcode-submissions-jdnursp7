class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, e in enumerate(nums):
            if target -e in map:
                return [map[target-e],i]
            map[e] = i
        