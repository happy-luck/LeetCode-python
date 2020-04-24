方法一：
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        j = 0
        for i in t:
            if i==s[j]:
                j += 1
            if j==len(s):
                return True
        return False
方法二：
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        b = iter(t)   # 把 t 转化成了一个迭代器
        return all(((i in b) for i in s))