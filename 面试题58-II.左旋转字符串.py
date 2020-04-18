class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = s+s[:n]
        return s[n:]

时间复杂度 O(N) ： 其中 N 为字符串 s 的长度，字符串切片函数为线性时间复杂度（参考资料）；
空间复杂度 O(N) ： 两个字符串切片的总长度为 N  