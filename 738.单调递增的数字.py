方法一：
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digits = []
        A = list(map(int, str(N)))
        for i in range(len(A)):
            for d in range(1, 10):
                if digits + [d] * (len(A)-i) > A:
                    digits.append(d-1)
                    break
            else:
                digits.append(d)
        return int("".join(map(str, digits)))
时间复杂度：O(D**2)。其中 D≈logN，N 是数字的长度，我们花费 O(D) 的时间构建数字和 O(D) 的时间比较每个候选答案。
空间复杂度：O(D)，答案和临时字符串的大小

方法二：
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        S = list(str(N))
        i = 1
        while i < len(S) and S[i-1] <= S[i]:
            i += 1
        while 0 < i < len(S) and S[i-1] > S[i]:
            S[i-1] = str(int(S[i-1]) - 1)
            i -= 1
        S[i+1:] = '9' * (len(S) - i-1)
        return int("".join(S))
时间复杂度：O(D)。其中 D≈logN，N 是数字的长度。
空间复杂度：O(D)，答案所使用的空间。 