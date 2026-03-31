class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = {}
        char_t = {}
        for char in s:
            char_s[char] = char_s.get(char,0) + 1
        for char in t:
            char_t[char] = char_t.get(char,0) + 1
        return (len(s)==len(t) and char_s == char_t)
        
        