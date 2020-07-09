方法一：
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)-1):
            j = i+1
            while(j<len(prices)):
                if prices[j]<=prices[i]:
                    res.append(prices[i]-prices[j])
                    break
                j += 1
            if j==len(prices):
                res.append(prices[i])
        res.append(prices[-1])
        return res
方法二：单调栈
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n =len(prices)
        stack=[]
        res=[prices[i] for i in range (n)]#不重新创建这个列表也可，python只是不能直接修改字符串
        for i in range(n):
       '''
用while循环是因为要一直出栈，溯回到不满足当前数字比栈顶元素小，将比当前大的数字全部出栈，最后将元素本身也要入栈 
'''
            while(stack and prices[i]<=prices[stack[-1]]):#stack[-1]表示栈顶数据
                res[stack[-1]] -= prices[i]#找到第一个比栈顶元素小的数字，做减法
                stack.pop()#弹出栈顶数字，然后循环这个操作，将当前的数字和栈中下一个数字比较
            stack.append(i)#将下标进栈
        return res