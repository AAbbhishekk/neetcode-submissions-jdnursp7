class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        import heapq

        heap=[]

        for num in nums:
            if num in heap:
                return num
            else:
                heapq.heappush(heap,num)
        