class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n=len(nums)
        res,sol=[],[]

        def backtrack(i,cursum):

            #basecase
            if cursum==target:
                res.append(sol[:])
                return

            if cursum > target or i ==n:
                return

            
            #not choose
            backtrack(i+1,cursum)

            
            sol.append(nums[i])
            backtrack(i , cursum+nums[i])
            sol.pop()


        backtrack(0,0)

        return res
        