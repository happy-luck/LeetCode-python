class Solution:
    def minCount(self, coins: List[int]) -> int:
        res = 0
        for c in coins:
            if c%2==0:
                res += c//2
            else:
                res = res + c//2 + 1
        return res