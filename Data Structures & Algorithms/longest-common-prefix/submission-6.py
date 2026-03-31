class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)

        l = 0
        
        res=''

        while l <= len(strs[0])-1 and strs[0][l] ==strs[-1][l]:
            res=res+strs[0][l]
            l = l +1
        
        return res
        