class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0

        def time_to_eat_banana(k):
            time_taken = 0
            for pile in piles:
                time_taken +=math.ceil(pile/k)
            return time_taken

        while l <=r:
            k = (l+r)//2

            if time_to_eat_banana(k) <= h:
                res = k
                r = k -1
                
            else:
                l = k + 1
                
        
        return res
        