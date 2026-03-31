class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)

        cursum=sum(cardPoints[:n-k])
        minsum=cursum

        for i in range(n-k,n):
            cursum = cursum + cardPoints[i]
            cursum = cursum - cardPoints[i-n+k]
            minsum = min(minsum,cursum)

        return sum(cardPoints) - minsum

        