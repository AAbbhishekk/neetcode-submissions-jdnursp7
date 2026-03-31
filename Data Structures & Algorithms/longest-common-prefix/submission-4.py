class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)

        l = 0
        r= len(strs[0])-1
        res=''

        while l <= r and strs[0][l] ==strs[-1][l]:
            res=res+strs[0][l]
            l = l +1
        
        return res
        