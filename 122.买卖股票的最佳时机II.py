方法一：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                max_ += prices[i] - prices[i-1]
        return max_
时间复杂度：O(n)，遍历一次。
空间复杂度：O(1)，需要常量的空间。

方法二：峰谷法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        valley = prices[0]
        peak = prices[0]
        max_ = 0
        while(i<len(prices)-1):
            while i<len(prices)-1 and prices[i+1]<=prices[i]:
                i += 1
            valley = prices[i]
            while i<len(prices)-1 and prices[i+1]>=prices[i]:
                i += 1
            peak = prices[i]
            max_ += peak - valley
        return max_
时间复杂度：O(n)。遍历一次。
空间复杂度：O(1)。需要常量的空间。        