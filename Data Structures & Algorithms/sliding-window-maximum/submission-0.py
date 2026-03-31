class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []
        for i in range(len(nums)-k+1):
            temp_list = nums[i:i+k]
            max_list.append(max(temp_list))
        return max_list
        