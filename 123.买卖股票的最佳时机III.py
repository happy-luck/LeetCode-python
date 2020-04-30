方法一：
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_buy, first_sell, second_buy, second_sell = -sys.maxsize, 0, -sys.maxsize, 0
        for price in prices:
            first_buy = max(first_buy, -price)  # 第一次买入手上的钱
            first_sell = max(first_sell, price+first_buy)  # 第一次卖出手上的钱
            second_buy = max(second_buy, first_sell-price)  # 第二次买入手上的钱
            second_sell = max(second_sell, price+second_buy)  # 第二次卖出手上的钱
        return second_sell

方法二：划分
我们分别使用 f(i) 和 g(i) 保存两段的最大利润，最后计算两段和的最大值。对于每一段的利润，按照 股票问题一思路2 计算即可。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        f = [0 for _ in range(n)] # 保存第i天最大利润
        g = [0 for _ in range(n)] 
        # 计算 1 ~ i 
        minprice = prices[0]
        for i in range(1, n): 
            f[i] = max(f[i - 1], prices[i] - minprice) # 完整交易出现在前 i-1 天里，或者第i天
            minprice = min(minprice, prices[i])
        # 计算 i ~ n，倒序遍历
        maxprice = prices[n - 1]
        for j in range(n - 2, -1, -1):
            g[j] = max(g[j + 1], maxprice - prices[j])  # 完整交易出现在 j 之后几天里，或者第j天
            maxprice = max(maxprice, prices[j])
        # 取两次交易的最大值
        res = max(f[n - 1], g[0]) # 交易一次
        for i in range(1, n - 2):
            res = max(f[i] + g[i + 1], res)
        return res
时间复杂度：O(n)。
空间复杂度：O(n)。

方法三：动态规划
思考一个状态方程，大致分三步：
					状态表示
					状态属性
					状态计算
1. 状态表示
很容易想到，可用 dp(i,j) 表示第 i 天进行 j 次交易的最大利润。
2. 状态属性
可以看到题目要求是最大利润，所以属性就是求一个最大值。
3. 状态计算
i 天可以划分两种情况：
不交易：第 i 天什么都没发生，交易次数 j 不变，利润为前一天的利润：
dp(i,j)=dp(i−1,j)
交易：利润为前 j−1 次交易的利润与第 i 天交易的利润之和：
dp(i,j)= dp(k−1,j−1)+ prices(i)−prices(k)
​结合就是：
dp(i,j)= prices(i) − (prices(k)−dp(k−1,j−1))
​
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        row, col = len(prices), 3
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for j in range(1, 3):
            mincost = prices[0] # 初始化成本为第一天的价格
            for i in range(1, row):
                mincost = min(mincost, prices[i] - dp[i - 1][j - 1]) # 买-利润=卖之前的成本
                dp[i][j] = max(dp[i - 1][j], prices[i] - mincost)
        return dp[row - 1][2]

时间复杂度：O(2n)。
空间复杂度：O(3n)。