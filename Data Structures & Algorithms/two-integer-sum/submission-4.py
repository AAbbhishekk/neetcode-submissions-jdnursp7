class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,e in enumerate(nums):
            if target - e in a:
                return [a[target-e],i]
            a[e] = i
        

            
        