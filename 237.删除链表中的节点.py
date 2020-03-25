class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
时间和空间复杂度都是：O(1)