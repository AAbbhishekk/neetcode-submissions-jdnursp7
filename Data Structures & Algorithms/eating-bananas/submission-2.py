class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r=max(piles)
        res = r
        
        def time_to_eat_piles(piles, k):
            times = 0
            for p in piles:
                times= times + (math.ceil(p/k))
            return times

        l = 1
        
        while l<=r:
            k = (l+r)//2
        

            if time_to_eat_piles(piles,k) <=h:
                res = k
                r = k - 1
            else:
                l = k +1
        return res