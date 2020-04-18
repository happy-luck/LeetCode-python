方法一：
class Solution:
    def sumNums(self, n: int) -> int:
        return n and n+self.sumNums(n-1) 

方法二：
class Solution:
    def sumNums(self, n: int) -> int:
        if n==0:
            return 0
        return n+self.sumNums(n-1) 