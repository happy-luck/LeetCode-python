方法一：
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur = head
        dic = {}
        while(cur):
            if cur in dic:
                return True
            dic[cur] = 1
            cur = cur.next
        return False
时间复杂度：O(n)，对于含有 n 个元素的链表，我们访问每个元素最多一次。添加一个结点到哈希表中只需要花费 O(1) 的时间。
空间复杂度：O(n)，空间取决于添加到哈希表中的元素数目，最多可以添加 n 个元素。

方法二：
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while(slow!=fast):
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True    

时间复杂度：O(n)，让我们将 n 设为链表中结点的总数。为了分析时间复杂度，我们分别考虑下面两种情况。
空间复杂度：O(1)，我们只使用了慢指针和快指针两个结点，所以空间复杂度为 O(1)。
