from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        z= []
        a = Counter(nums)
        a = {k: v for k, v in sorted(a.items(), key=lambda item: item[1])}
        return list(a)[::-1][:k]
        
        

        
        