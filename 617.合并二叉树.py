方法一：递归

我们可以对这两棵树同时进行前序遍历，并将对应的节点进行合并。在遍历时，如果两棵树的当前节点均不为空，我们就将它们的值进行相加，并对它们的左孩子和右孩子进行递归合并；如果其中有一棵树为空，那么我们返回另一颗树作为结果；如果两棵树均为空，此时返回任意一棵树均可（因为都是空）。

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t2==None:
            return t1
        if t1==None:
            return t2
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        return t1
时间复杂度：O(N)，其中 N 是两棵树中节点个数的较小值。
空间复杂度：O(N)，在最坏情况下，会递归 N 层，需要 O(N) 的栈空间。

方法二：迭代
我们首先把两棵树的根节点入栈，栈中的每个元素都会存放两个根节点，并且栈顶的元素表示当前需要处理的节点。在迭代的每一步中，我们取出栈顶的元素并把它移出栈，并将它们的值相加。随后我们分别考虑这两个节点的左孩子和右孩子，如果两个节点都有左孩子，那么就将左孩子入栈；如果只有一个节点有左孩子，那么将其作为第一个节点的左孩子；如果都没有左孩子，那么不用做任何事情。对于右孩子同理。

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t2==None:
            return t1
        if t1==None:
            return t2
        stack = [(t1,t2)]
        while stack:
            t = stack.pop(0)
            if t[1]==None:
                continue
            t[0].val += t[1].val
            if(t[0].left==None):
                t[0].left = t[1].left
            else:
                stack.append((t[0].left,t[1].left))
            if(t[0].right==None):
                t[0].right = t[1].right
            else:
                stack.append((t[0].right,t[1].right))
        return t1

时间复杂度：O(N)，其中 N 是两棵树中节点个数的较小值。
空间复杂度：O(N)，在最坏情况下，栈中会存放 N 个节点。
