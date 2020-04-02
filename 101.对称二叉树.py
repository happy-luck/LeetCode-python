方法一：递归

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return self.judge(root.left,root.right)
        else:
            return True
    def judge(self,l,r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val==r.val:
            return self.judge(l.left,r.right) and self.judge(l.right,r.left)
        return False
时间复杂度：O(n)，因为我们遍历整个输入树一次，所以总的运行时间为 O(n)，其中 n 是树中结点的总数。
空间复杂度：递归调用的次数受树的高度限制。在最糟糕情况下，树是线性的，其高度为 O(n)。因此，在最糟糕的情况下，由栈上的递归调用造成的空间复杂度为 O(n)。

方法二：迭代
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root.left,root.right]
        while queue:
            l = queue.pop()
            r = queue.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            queue.append(l.left)
            queue.append(r.right)
            queue.append(l.right)
            queue.append(r.left)
        return True

时间复杂度：O(n)，因为我们遍历整个输入树一次，所以总的运行时间为 O(n)，其中 n 是树中结点的总数。
空间复杂度：搜索队列需要额外的空间。在最糟糕情况下，我们不得不向队列中插入 O(n) 个结点。因此，空间复杂度为 O(n)。