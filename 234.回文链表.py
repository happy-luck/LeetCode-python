方法一:
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ls = []
        while(head):
            ls.append(head.val)
            head = head.next
        n = len(ls)
        for i in range(n//2):
            if ls[i] != ls[n-i-1]:
                return False
        return True

方法二：
def isPalindrome(self, head: ListNode) -> bool:
    vals = []
    current_node = head
    while current_node is not None:
        vals.append(current_node.val)
        current_node = current_node.next
    return vals == vals[::-1]

时间复杂度：O(n)，其中 n 指的是链表的元素个数。
第一步： 遍历链表并将值复制到数组中，O(n)。
第二步：双指针判断是否为回文，执行了 O(n/2) 次的判断，即 O(n)。
总的时间复杂度：O(2n)=O(n)。
空间复杂度：O(n)，其中 n 指的是链表的元素个数，我们使用了一个数组列表存放链表的元素值。

方法三：递归
def isPalindrome(self, head: ListNode) -> bool:
    self.front_pointer = head
    def recursively_check(current_node=head):
        if current_node is not None:
            if not recursively_check(current_node.next):
                return False
            if self.front_pointer.val != current_node.val:
                return False
            self.front_pointer = self.front_pointer.next
        return True

    return recursively_check()
时间复杂度：O(n)，其中 n 指的是链表的大小。
空间复杂度：O(n)，其中 n 指的是链表的大小。

方法四：

找到前半部分链表的尾节点。
反转后半部分链表。
判断是否为回文。
恢复链表。
返回结果。
执行步骤一，我们可以计算链表节点的数量，然后遍历链表找到前半部分的尾节点。
或者可以使用快慢指针在一次遍历中找到：慢指针一次走一步，快指针一次走两步，快慢指针同时出发。当快指针移动到链表的末尾时，慢指针到链表的中间。通过慢指针将链表分为两部分。
若链表有奇数个节点，则中间的节点应该看作是前半部分。
步骤二可以使用在反向链表问题中找到解决方法来反转链表的后半部分。
步骤三比较两个部分的值，当后半部分到达末尾则比较完成，可以忽略计数情况中的中间节点。
步骤四与步骤二使用的函数相同，再反转一次恢复链表本身。

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next
        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result    
    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

时间复杂度：O(n)，其中 n 指的是链表的大小。
空间复杂度：O(1)，我们是一个接着一个的改变指针，我们在堆栈上的堆栈帧不超过 O(1)。
该方法的缺点是，在并发环境下，函数运行时需要锁定其他线程或进程对链表的访问，因为在函数执执行过程中链表暂时断开。
