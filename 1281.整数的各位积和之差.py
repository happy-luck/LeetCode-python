class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        add = 0
        while(n>0):
            x = n%10
            mul *= x
            add += x
            n //= 10 
        return mul-add

时间复杂度：O(logN)。整数 N 的位数为 ⌈log 10(N+1)⌉，根据换底公式，它和时间复杂度中常用的以 2 为底的 log 只相差一个常数，因此可以表示为 O(logN)。

空间复杂度：O(1)。