class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0]*len(temperatures)
        stack=[] #value,id

        for i, e in enumerate(temperatures):

            while stack and e>stack[-1][0]:
                lastValue, lastId = stack.pop()
                res[lastId] = i - lastId

            stack.append((e,i))

        
        return res
        