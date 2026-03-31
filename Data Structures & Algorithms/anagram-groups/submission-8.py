class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagram_dict = defaultdict(list)

        for word in strs:
            k = "".join(sorted(word))

            print(k)
            anagram_dict[k].append(word)
            


        return list(anagram_dict.values())
        