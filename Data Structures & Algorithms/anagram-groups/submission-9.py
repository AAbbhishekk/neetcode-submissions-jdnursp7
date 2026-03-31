class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagram_dict = defaultdict(list)

        for word in strs:
            temp = [0]*26
            for char in word:
                temp[ord(char)-ord('a')]+=1
            tuple(temp)
            anagram_dict[tuple(temp)].append(word)
            


        return list(anagram_dict.values())
        