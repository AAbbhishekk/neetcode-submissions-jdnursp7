class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen=0
        output=''

        for i in range(len(s)):

            #odd len
            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1>maxlen:
                    maxlen=r-l+1
                    output = s[l:r+1]
                l=l-1
                r=r+1


            #even len
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1>maxlen:
                    maxlen=r-l+1
                    output = s[l:r+1]
                l=l-1
                r=r+1
        
        return output
                
        