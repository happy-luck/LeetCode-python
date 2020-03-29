方法一: 暴力法

对链表A中的每一个结点 ai，遍历整个链表 B 并检查链表 B 中是否存在结点和 ai相同。

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        while(pA):
            pB = headB
            while(pB):
                if pA == pB:
                    return pA
                pB = pB.next
            pA = pA.next
        return None

时间复杂度 : (mn)。
空间复杂度 : O(1)。



方法二: 哈希表法

遍历链表 A 并将每个结点的地址/引用存储在哈希表中。然后检查链表 B 中的每一个结点 bi是否在哈希表中。若在，则 bi为相交结点。
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        hashA  = {}
        while headA:
            hashA[headA] = 1
            headA = headA.next
        while headB:
            if hashA.get(headB) is not None:
                return headB
            headB = headB.next

时间复杂度 : O(m+n)。
空间复杂度 : O(m) 或 O(n)。



方法三：双指针法
创建两个指针 pA 和 pB，分别初始化为链表 A 和 B 的头结点。然后让它们向后逐结点遍历。
当 pA 到达链表的尾部时，将它重定位到链表 B 的头结点 (你没看错，就是链表 B); 类似的，当 pB 到达链表的尾部时，将它重定位到链表 A 的头结点。
若在某一时刻 pA 和 pB 相遇，则 pA/pB 为相交结点。
想弄清楚为什么这样可行, 可以考虑以下两个链表: A={1,3,5,7,9,11} 和 B={2,4,9,11}，相交于结点 9。 由于 B.length (=4) < A.length (=6)，pB 比 pA 少经过 2 个结点，会先到达尾部。将 pB 重定向到 A 的头结点，pA 重定向到 B 的头结点后，
pB 要比 pA 多走 2 个结点。因此，它们会同时到达交点。
如果两个链表存在相交，它们末尾的结点必然相同。因此当 pA/pB 到达链表结尾时，记录下链表 A/B 对应的元素。若最后元素不相同，则两个链表不相交。
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA == None or headB == None):
             return None
        pA = headA
        pB = headB
        while (pA != pB):
            pA = (headB if (pA == None) else pA.next)
            pB = (headA if (pB == None) else pB.next)
        return pA
时间复杂度 : O(m+n)。
空间复杂度 : O(1)。