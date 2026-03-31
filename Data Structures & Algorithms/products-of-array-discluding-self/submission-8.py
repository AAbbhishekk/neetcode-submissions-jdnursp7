class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_multi =1
        r_multi = 1
        lst1 =[0]*len(nums)
        lst2 =[0]*len(nums)

        for i in range(len(nums)):
            j = -i-1
            lst1[i] = l_multi
            lst2[j] = r_multi

            l_multi = l_multi*nums[i]
            r_multi = r_multi*nums[j]

        return [a*b for a,b in zip(lst1,lst2)]        