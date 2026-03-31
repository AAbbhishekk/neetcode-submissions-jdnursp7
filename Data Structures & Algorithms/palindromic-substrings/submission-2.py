class Solution:
    def countSubstrings(self, s: str) -> int:

        def checkpalindrome(n):
            count = 0

            for i in range(len(n)):
                # count = 0
                #odd len
                l=i
                r=i

                while l>=0 and r<len(n) and n[l]==n[r]:
                    count = count+1

                    l=l-1
                    r=r+1
                
                #odd len
                l=i
                r=i+1

                while l>=0 and r<len(n) and n[l]==n[r]:
                    count = count+1

                    l=l-1
                    r=r+1
            
            return count
        return checkpalindrome(s)
    
                


        