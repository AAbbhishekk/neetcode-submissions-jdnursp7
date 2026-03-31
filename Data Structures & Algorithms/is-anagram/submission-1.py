class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a,b = {},{}
        for elem in s:
            if elem not in a:
                a[elem] = 1
            else:
                a[elem] = a[elem] + 1
        for elem in t:
            if elem not in b:
                b[elem] = 1
            else:
                b[elem] = b[elem] + 1
        if a ==b:
            return True
        else:
            return False

        
        