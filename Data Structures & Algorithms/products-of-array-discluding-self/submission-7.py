class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prefix = [0]*len(nums)
        r_prefix = [0]*len(nums)
        cursum = 1

        for i in range(len(nums)):
            l_prefix[i] = cursum
            cursum = cursum*nums[i]

        cursum = 1
        for i in range(len(nums)):
            r_prefix[-i-1]=cursum
            cursum = cursum*nums[-i-1]

        return [a*b for a,b in zip(l_prefix,r_prefix)]

