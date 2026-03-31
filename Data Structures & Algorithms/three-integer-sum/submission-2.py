class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i , e in enumerate(nums):
            if e>0:
                break
            if i>0 and e==nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l <r:
                if e +nums[l]+nums[r]>0:
                    r=r-1
                elif e+nums[l]+nums[r]<0:
                    l=l+1
                else:
                    res.append([e,nums[l],nums[r]])
                    l =l+1
                    r=r-1
                    while nums[l]==nums[l-1] and l<r:
                        l=l+1
        return res
        