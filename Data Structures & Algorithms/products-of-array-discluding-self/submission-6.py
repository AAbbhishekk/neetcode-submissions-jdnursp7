class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[0]*len(nums)
        r=[0]*len(nums)

        prod_l=1
        for i in range(len(nums)):
            l[i] = prod_l
            prod_l = prod_l*nums[i]
        prod_r = 1
        for i in range(len(nums)):
            j = -i-1
            r[j] = prod_r
            prod_r =prod_r*nums[j]

        return [a*b for a, b in zip(l,r)]
        