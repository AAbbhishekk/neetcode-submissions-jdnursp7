class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        
        water = 0

        l=0
        r = len(height)-1

        maxleft = height[l]
        maxright = height[r]

        while l < r:
            if maxleft < maxright:
                l = l+1
                maxleft = max(maxleft,height[l])
                water += maxleft - height[l]
                # l = l+1
            else:
                r = r-1
                maxright = max(maxright,height[r])
                water += maxright - height[r]
                

        return water
        