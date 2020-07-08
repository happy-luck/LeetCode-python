方法一：
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = bin(x)
        y_bin = bin(y)
        if len(x_bin)>len(y_bin):
            n = len(x_bin)-2
            m = len(y_bin)-2
            y_bin,x_bin = x_bin,y_bin
        else:
            m = len(x_bin)-2
            n = len(y_bin)-2
        res = 0
        for i in range(m):
            if(x_bin[i+2]!=y_bin[i+n-m+2]):
                res += 1
        for i in range(n-m):
            if(y_bin[i+2]!='0'):
                res += 1
        return res

方法二：内置位计数功能
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
时间复杂度：O(1)。
该算法有两个操作。计算 XOR 花费恒定时间。
调用内置的 bitCount 函数。最坏情况下，该函数复杂度为O(k)，其中 k是整数的位数。
在 Python 和 Java 中 Integer 是固定长度的。因此该算法复杂度恒定，与输入大小无关。
空间复杂度：O(1)，使用恒定大小的空间保存 XOR 的结果。
假设内置函数也使用恒定空间。

方法三：移位
采用右移位，每个位置都会被移动到最右边。移位后检查最右位的位是否为 1 即可。
检查最右位是否为 1，可以使用取模运算（i % 2）或者 AND 操作（i & 1），
这两个操作都会屏蔽最右位以外的其他位。
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        distance = 0
        while xor:
            # mask out the rest bits
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance
时间复杂度：O(1)，在 Python 和 Java 中 Integer 的大小是固定的，处理时间也是固定的。
32 位整数需要 32 次迭代。
空间复杂度：O(1)，使用恒定大小的空间。

方法四：布赖恩·克尼根算法
像人类直观的计数比特为 1 的位数，跳过两个 1 之间的 0。
布赖恩·克尼根位计数算法的基本思想。该算法使用特定比特位和算术运算移除等于 1 的最右比特位。
当我们在 number 和 number-1 上做 AND 位运算时，原数字 number 的最右边等于 1 的比特会被移除。
class Solution:
    def hammingDistance(self, x, y):
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            # remove the rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance
时间复杂度：O(1)。
与移位方法相似，由于整数的位数恒定，因此具有恒定的时间复杂度。
但是该方法需要的迭代操作更少。
空间复杂度：O(1)，与输入无关，使用恒定大小的空间。