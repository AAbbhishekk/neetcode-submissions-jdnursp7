class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        # Frequency count of characters in s1
        s1_count = Counter(s1)
        window_count = Counter()

        w_size = len(s1)
        for i, char in enumerate(s2):
            # Add the current character to the window
            window_count[char] += 1

            # Remove the character that is out of the window's size
            if i >= w_size:
                left_char = s2[i - w_size]
                if window_count[left_char] == 1:
                    del window_count[left_char]
                else:
                    window_count[left_char] -= 1

            # Compare window's frequency count with s1's frequency count
            if window_count == s1_count:
                return True

        return False
