class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        base_counter = Counter(s1)
        win_size = len(s1)
        new_counter = Counter()

        for i,char in enumerate(s2):
            new_counter[char]=new_counter[char]+1

            if i >=win_size:
                left_char = s2[i-win_size]
                if new_counter[left_char]==1:
                    del new_counter[left_char]
                else:
                    new_counter[left_char]=new_counter[left_char]-1
            if base_counter == new_counter:
                return True
        return False


        