方法一：
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        D = 0
        A_list = []
        for string in A:
            res = list(string)
            res = [ord(i) for i in res]
            A_list.append(res)
        for j in range(len(res)):
            for i in range(1,len(A)):
                if A_list[i][j]-A_list[i-1][j]<0:
                    D += 1
                    break
        return D

方法二：
class Solution(object):
    def minDeletionSize(self, A):
        ans = 0
        for col in zip(*A):
            if any(col[i] > col[i+1] for i in xrange(len(col) - 1)):
                ans += 1
        return ans

时间复杂度：O(N)，其中 N 是数组 A 中的元素个数。
空间复杂度：O(1)。 