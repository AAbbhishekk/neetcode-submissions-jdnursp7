class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        water = 0
        l,r = 0,len(heights)-1
        while l<r:
            water = (r-l)*min(heights[l],heights[r])
            maximum = max(water,maximum)
            if heights[l]<=heights[r]:
                l=l+1
            else:
                r=r-1
        return maximum
            
        


        