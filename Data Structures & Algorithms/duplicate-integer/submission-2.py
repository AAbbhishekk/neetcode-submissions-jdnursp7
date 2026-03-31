class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for item in nums:
            if item not in a.keys():
                a[item] = 1
            else:
                a[item] = a[item] + 1
        if len(a.keys()) == len(nums):
            return False
        else:
            return True
         