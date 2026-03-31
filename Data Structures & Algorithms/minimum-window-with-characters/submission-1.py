class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)==0:
            return ""
        countT={}
        for c in t:
            countT[c] = countT.get(c,0) + 1
        window={}
        have = 0
        need = len(countT)
        res=[-1,-1]
        reslen= float("inf")

        l=0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have = have+1
            
            while have == need:
                if (r-l+1)<reslen:
                    res = [l,r]
                    reslen=r-l+1
                window[s[l]] = window[s[l]]-1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have=have-1
                l=l+1
        l,r = res

        return s[l:r+1] if reslen!=float("inf") else ""

