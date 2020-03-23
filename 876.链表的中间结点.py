方法一：
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cur = head
        p = head
        num = 0
        while cur:
            num += 1
            cur = cur.next
        mid = num // 2
        while mid:
            p = p.next
            mid -= 1
        return p
时间复杂度：O(N)，其中 N 是给定链表的结点数目。
空间复杂度：O(1)，只需要常数空间存放变量和指针。

方法二：数组

思路和算法

链表的缺点在于不能通过下标访问对应的元素。因此我们可以考虑对链表进行遍历，同时将遍历到的元素依次放入数组 A 中。如果我们遍历到了 N 个元素，那么链表以及数组的长度也为 N，对应的中间节点即为 A[N/2]。

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]

时间复杂度：O(N)，其中 N 是给定链表中的结点数目。
空间复杂度：O(N)，即数组 A 用去的空间。

方法三：快慢指针法
思路和算法

我们可以继续优化方法一，用两个指针 slow 与 fast 一起遍历链表。slow 一次走一步，fast 一次走两步。那么当 fast 到达链表的末尾时，slow 必然位于中间。

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

时间复杂度：O(N)，其中 N 是给定链表的结点数目。
空间复杂度：O(1)，只需要常数空间存放 slow 和 fast 两个指针。