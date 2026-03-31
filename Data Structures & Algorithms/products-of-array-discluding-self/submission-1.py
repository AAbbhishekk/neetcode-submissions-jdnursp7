class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =len(nums)
        l_arr=[0]*n
        r_arr=[0]*n
        l_s =1
        r_s =1
        for i in range(n):
            j = -i - 1
            l_arr[i]=l_s
            r_arr[j]=r_s
            l_s = l_s * nums[i]
            r_s = r_s * nums[j]

        return [a*b for a,b in zip(l_arr,r_arr)]

        