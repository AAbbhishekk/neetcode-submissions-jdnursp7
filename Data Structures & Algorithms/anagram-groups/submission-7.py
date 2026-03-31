class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagram_dict = defaultdict(list)

        for s in strs:
            temp = [0]*26
            for c in s:
                temp[ord(c)-ord('a')]+=1
            
            temp = tuple(temp)
            anagram_dict[temp].append(s)

        return list(anagram_dict.values())
        