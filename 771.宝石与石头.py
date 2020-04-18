方法一：
class Solution(object):
    def numJewelsInStones(self, J, S):
        return sum(s in J for s in S)

时间复杂度：O(J.length∗S.length)。
空间复杂度：在 Python 实现中，空间复杂度为 O(1)。在 Java 实现中，空间复杂度为 O(J.length∗S.length)。

方法二：
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        res = 0
        for s in S:
            if s in J:
                res += 1
        return res

时间复杂度：O(J.length+S.length)。O(J.length) 这部分来自于创建 J，O(S.length) 这部分来自于搜索 S。
空间复杂度：O(J.length)
