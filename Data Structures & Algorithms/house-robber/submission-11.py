class Solution:
    def rob(self, nums: List[int]) -> int:
        n1,n2 =0,0

        for num in nums:
            temp = max(num+n1,n2)
            n1=n2
            n2=temp

        return n2