class Solution:
    def climbStairs(self, n: int) -> int:
        curr = 2
        prev = 1

        if n<=2:
            return n

        for _ in range(3,n+1):
            temp = prev + curr
            prev = curr
            curr = temp

        return curr
