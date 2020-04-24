class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minprice = prices[0]
        maxprofit = 0
        for p in prices:
            maxprofit = max(maxprofit,p-minprice)
            minprice = min(minprice,p)
        return maxprofit
时间复杂度：O(n)，只需要遍历一次。
空间复杂度：O(1)，只使用了常数个变量。        