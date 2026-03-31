class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = {}
        char_t = {}
        if len(s) != len(t):
            return False
        for char in range(len(s)):
            char_s[s[char]] = char_s.get(s[char],0) + 1
        
            char_t[t[char]] = char_t.get(t[char],0) + 1
        return (len(s)==len(t) and char_s == char_t)
        
        