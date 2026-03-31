class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_sum = [0]*len(nums)
        r_sum =[0]*len(nums)
        l_s=1
        r_s=1
        for i in range(len(nums)):
            j=-i-1
            l_sum[i]=l_s
            r_sum[j]=r_s
            l_s = l_s*nums[i]
            r_s =r_s*nums[j]
        return[a*b for a,b in zip(l_sum,r_sum)]
        