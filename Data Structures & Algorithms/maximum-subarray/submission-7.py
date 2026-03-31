class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsum=float("-inf")

        cursum = 0

        for i in range(len(nums)):
            cursum = cursum + nums[i]
            maxsum = max(maxsum, cursum)

            if cursum < 0:
                cursum = 0
        
        return maxsum

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         cursum = nums[0]
#         maxsum=cursum

#         for i in range(1,len(nums)):
#             cursum = max(nums[i],cursum+nums[i])
#             maxsum = max(maxsum,cursum)


#         return maxsum
        