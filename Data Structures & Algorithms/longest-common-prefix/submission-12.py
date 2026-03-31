class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        res=''

        l=0
        
        r = len(strs[0])

        while l<=len(strs[0])-1 and strs[0][l]==strs[-1][l]:

            res=strs[0][:l+1]
            l=l+1
            # l=l+1

        return res

        
        