class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l=0
        length = 0
        map = {}

        for r in range(len(s)):
            if s[r] in map:
                l = max(map[s[r]]+1,l)
            map[s[r]] = r
            length = max(length, r-l+1)
        return length
        