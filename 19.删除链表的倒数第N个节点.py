# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        Node = ListNode(None)
        Node.next = head
        fast,slow = Node,Node
        for i in range(n):
            fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next 
        return Node.next
