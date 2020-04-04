方法一：
class Solution:
    def maximum69Number (self, num: int) -> int:
        n = 0
        t = num
        tar = -1
        while t:
            m = t%10
            t = t//10
            if m==6:
                tar = n
            n += 1
        if tar!=-1:
            res = num + 3*(10**tar)
            return res
        else:
            return num

方法二：
class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))
        
时间复杂度：O(lognum)，表示 num 的位数。
空间复杂度：O(lognum)。为了代码编写方便，我们使用额外的字符串来存储 num，使得可以直接修改特定位置的数字。            