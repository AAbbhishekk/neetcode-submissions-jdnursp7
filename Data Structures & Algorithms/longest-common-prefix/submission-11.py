class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        
        l = 0
        res=''

        while l <= len(strs[0])-1 and strs[0][l] ==strs[-1][l]:
            res=strs[0][:l+1]
            l = l +1
        
        return res
        