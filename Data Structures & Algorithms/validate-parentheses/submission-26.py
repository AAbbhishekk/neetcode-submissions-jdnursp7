class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")":"(","]":"[","}":"{"}

        for i in range(len(s)):
            if s[i] not in map:
                stack.append(s[i])
            else:
                # print(stack)
                print(stack)
                print(s[i])
                if not stack or stack[-1]!=map[s[i]]:
                    return False
                stack.pop()
        # print(stack)
        return len(stack)==0
        