class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        line = [1,1]
        while line[-1]<k:
            line.append(line[-1]+line[-2])
        ans = 0
        for i in line[::-1]:
            if k>=i:
                ans+=1
                k -= i
        return ans
时间复杂度：O(44)。不超过 10**9的斐波那契数一共有 44 个。
空间复杂度：O(44)。