class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagram_dict = defaultdict(list)
        for s in strs:
            temp = "".join(sorted(s))
            anagram_dict[temp].append(s)


        return list(anagram_dict.values())
        