class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagramdict = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] +=1

            k = tuple(count)

            anagramdict[k].append(s)

        return list(anagramdict.values())
