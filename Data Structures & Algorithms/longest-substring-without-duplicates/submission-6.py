class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        l=0
        res=0
        n = len(s)
        for i in range(n):
            while s[i] in sett:
                sett.remove(s[l])
                l=l+1
            sett.add(s[i])
            res = max(res,i-l+1)

        return res
